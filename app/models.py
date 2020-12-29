from django.db import models


class User(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(null=False, max_length=50)
    lastname = models.CharField(null=False, max_length=100)
    password = models.CharField(null=False, max_length=30)
    phone = models.CharField(unique=True, null=True, max_length=10)

    def __str__(self):
        return self.email


class Bike(models.Model):
    id = models.CharField(primary_key=True, max_length=150)
    title = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=500, null=True)
    brand = models.CharField(max_length=100, null=True)
    size = models.CharField(choices=(('12', '12'), ('16', '16'), ('20', '20'), ('24', '24'), ('26', '26')), null=True, max_length=2)

    img1 = models.ImageField(null=True, upload_to=f'bikes_img')
    img2 = models.ImageField(null=True, upload_to=f'bikes_img')
    img3 = models.ImageField(null=True, upload_to=f'bikes_img')
    img4 = models.ImageField(null=True, upload_to=f'bikes_img')

    bike = models.ManyToManyField('User', through='Cart_Bike')

    def __str__(self):
        return self.title


class Accessories(models.Model):
    id = models.CharField(primary_key=True, max_length=150)
    title = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=20, null=True, choices=(('helmet', 'Helmet'), ('clothes', 'Clothes'), ('flask', 'Flask'), ('gloves', 'Gloves')))

    img1 = models.ImageField(null=True, upload_to=f'accessories_img')
    img2 = models.ImageField(null=True, upload_to=f'accessories_img')
    img3 = models.ImageField(null=True, upload_to=f'accessories_img')
    img4 = models.ImageField(null=True, upload_to=f'accessories_img')

    accessories = models.ManyToManyField('User', through='Cart_Accessories')

    def __str__(self):
        return self.title


class Cart_Bike(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=True)
    number_products = models.IntegerField(default=0)

    class Meta:
        unique_together = ['user', 'bike']

    def __str__(self):
        return self.user.email + ' - ' + self.bike.title + ' - ' + str(self.number_products)


class Cart_Accessories(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE, null=True)
    number_products = models.IntegerField(default=0)

    class Meta:
        unique_together = ['user', 'accessories']

    def __str__(self):
        return self.user.email + ' - ' + self.accessories.title + ' - ' + str(self.number_products)


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, max_length=100)
    email = models.EmailField(null=True)
    ticket = models.CharField(null=True, max_length=1000)

    def __str__(self):
        return self.email
