from django.contrib import admin
from .models import Bike
from .models import Accessories
from .models import User
from .models import Cart_Bike
from .models import Cart_Accessories
from .models import Ticket

admin.site.site_header = 'Hope Bike'
admin.site.register(Bike)
admin.site.register(Accessories)
admin.site.register(User)
admin.site.register(Cart_Bike)
admin.site.register(Cart_Accessories)
admin.site.register(Ticket)
