from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect
from django.template import Template, Context
from .models import *


def sign_checker(cookies):
    print(f'Cookies: {cookies}')
    keys = cookies.keys()
    if 'user_cookie' in keys:
        user_cookie = cookies['user_cookie'].split('-')

        email = user_cookie[0]
        password = user_cookie[1]
        name = user_cookie[2]

        message = f'Welcome {name}'
        return True, message
    else:
        message = ''
        return False, message


def index(request):
    return render(request, template_name='app/index.html', context=None)


def sign(request):
    if sign_checker(request.COOKIES)[0]:
        return HttpResponseRedirect(reverse('index'))

    else:
        global response, logged_in, there_is_email, status
        status = None
        there_is_email = False
        there_is_phone = False
        response = None
        logged_in = False

        if request.method == 'POST':
            req = request.POST
            if len(req) == 3:  # For sign-in
                email = req.get('email')
                password = req.get('password')

                db_passwords = User.objects.values_list('password')
                db_emails = User.objects.values_list('email')

                for iteration in range(len(db_emails)):
                    if email == db_emails[iteration][0] and password == db_passwords[iteration][0]:
                        logged_in = True
                        break
                    else:
                        logged_in = False

                if logged_in:
                    user_data = User.objects.filter(email=email)[0]
                    response = HttpResponseRedirect(redirect_to=reverse('index'))
                    user_cookie = user_data.email + '-' + user_data.password + '-' + user_data.name
                    response.set_cookie(key='user_cookie', value=user_cookie)
                else:
                    response = render(request, 'app/Sign.html', context={'status': 'Enter true email/password...'})

                return response

            elif len(req) == 7:  # For sign-up
                email = req.get('email')
                password = req.get('password')
                first_name = req.get('first_name')
                last_name = req.get('last_name')
                phone = req.get('phone')
                conf_password = req.get('conf_password')

                if password != conf_password:
                    status = 'Your passwords not the same...'

                else:
                    for db_email in User.objects.values_list('email'):
                        if email == db_email[0]:
                            status = 'You tried to register with repetitive email.\nTry other one.'
                            there_is_email = True
                            break
                    for db_phone in User.objects.values_list('phone'):
                        if phone == db_phone[0]:
                            status = 'You tried to register with repetitive phone number.\nTry other one.'
                            there_is_phone = True
                            break

                    if not there_is_email and not there_is_phone:
                        user = User(email=email, password=password, name=first_name, lastname=last_name, phone=phone)
                        user.save()
                        status = 'You registered!'

                print(status)
                return render(request, 'app/Sign.html', context={'status': status})

        else:
            return render(request, template_name='app/Sign.html', context=None)


def bikes(request):
    is_logged, message = sign_checker(request.COOKIES)
    bikes = Bike.objects.all()
    return render(request, template_name='app/bikes.html', context={'bikes': bikes, 'message': message})


def bike_desc(request, slug):
    is_logged, message = sign_checker(request.COOKIES)
    good = Bike.objects.filter(id=slug)[0]
    title = good.title
    price = good.price
    description = good.description
    size = good.size
    brand = good.brand
    img1_url = good.img1.url
    img2_url = good.img2.url
    img3_url = good.img3.url
    img4_url = good.img4.url
    return render(request, template_name='app/bike_description.html', context={'img1': img1_url, 'img2': img2_url,
                                                                       'img3': img3_url, 'img4': img4_url,
                                                                       'title': title, 'price': price,
                                                                       'description': description, 'slug': slug,
                                                                       'message': message, 'size': size, 'brand': brand})


def add_bike_to_cart(request, slug):
    cookies = request.COOKIES
    is_logged, message = sign_checker(cookies)

    if is_logged:
        cookies = cookies['user_cookie'].split('-')
        there_is_product = False

        bike_id = slug
        user_id = cookies[0]

        carts = Cart_Bike.objects.filter(user_id=user_id)
        print(carts)
        print('------------')

        for cart in carts:
            if cart.bike_id == bike_id:
                there_is_product = True
                cart.number_products += 1
                cart.save()
                break
            else:
                there_is_product = False

        if not there_is_product:
            cart = Cart_Bike()
            cart.user_id = user_id
            cart.bike_id = bike_id
            cart.number_products += 1

            cart.save()

        resp = HttpResponseRedirect(reverse('cart'))
    else:
        resp = HttpResponseRedirect(reverse('sign'))

    return resp


def cart(request):
    print(f'Request: {request.GET}')
    print('--------------------')
    if 'bikes' in request.GET:
        product_id = request.GET['bikes']
        cookies = request.COOKIES
        item_bike = Cart_Bike.objects.filter(bike_id=product_id, user_id=cookies['user_cookie'].split('-')[0])
        item_accessorie = Cart_Accessories.objects.filter(accessories_id=product_id, user_id=cookies['user_cookie'].split('-')[0])
        item_bike.delete()
        item_accessorie.delete()
        resp = HttpResponseRedirect(reverse('cart'))

    else:
        cookies = request.COOKIES
        is_logged, message = sign_checker(cookies)

        if is_logged:
            cart_bikes = Cart_Bike.objects.filter(user_id=cookies['user_cookie'].split('-')[0])
            cart_accessories = Cart_Accessories.objects.filter(user_id=cookies['user_cookie'].split('-')[0])
            final_fee = 0

            for each_cart in cart_bikes:
                final_fee += (each_cart.bike.price * each_cart.number_products)

            for each_cart in cart_accessories:
                final_fee += (each_cart.accessories.price * each_cart.number_products)

            resp = render(request, template_name='app/cart.html', context={'message': message, 'cart_bikes': cart_bikes,
                                                                           'cart_accessories': cart_accessories, 'final_fee': final_fee})
        else:
            resp = HttpResponseRedirect(reverse('sign'))

    return resp


def exit(request):
    resp = HttpResponseRedirect(reverse('index'))
    resp.delete_cookie('user_cookie')

    return resp


def contact(request):
    cookies = request.COOKIES
    is_logged, message = sign_checker(cookies)

    response = render(request, template_name='app/ContactUs.html', context={'message': message})

    return response


def send_ticket(request):
    ticket = request.GET
    name = ticket['name']
    email = ticket['email']
    ticket = ticket['ticket']

    new_ticket = Ticket()
    new_ticket.name = name
    new_ticket.email = email
    new_ticket.ticket = ticket
    new_ticket.save()

    response = HttpResponseRedirect(reverse('contact'))

    return response


def accessories(request):
    accessories = Accessories.objects.all()
    cookies = request.COOKIES
    is_logged, message = sign_checker(cookies)

    response = render(request, template_name='app/accessories.html', context={'accessories': accessories, 'message': message})

    return response

def accessories_desc(request, slug):
    is_logged, message = sign_checker(request.COOKIES)
    good = Accessories.objects.filter(id=slug)[0]
    title = good.title
    price = good.price
    description = good.description
    img1_url = good.img1.url
    img2_url = good.img2.url
    img3_url = good.img3.url
    img4_url = good.img4.url
    return render(request, template_name='app/accessory_description.html', context={'img1': img1_url, 'img2': img2_url,
                                                                       'img3': img3_url, 'img4': img4_url,
                                                                       'title': title, 'price': price,
                                                                       'description': description, 'slug': slug,
                                                                       'message': message})

def add_accessories_to_cart(request, slug):
    cookies = request.COOKIES
    is_logged, message = sign_checker(cookies)

    if is_logged:
        cookies = cookies['user_cookie'].split('-')
        there_is_product = False

        accessories_id = slug
        user_id = cookies[0]

        carts = Cart_Accessories.objects.filter(user_id=user_id)
        print(carts)
        print('------------')

        for cart in carts:
            if cart.accessories_id == accessories_id:
                there_is_product = True
                cart.number_products += 1
                cart.save()
                break
            else:
                there_is_product = False

        if not there_is_product:
            cart = Cart_Accessories()
            cart.user_id = user_id
            cart.accessories_id = accessories_id
            cart.number_products += 1

            cart.save()

        resp = HttpResponseRedirect(reverse('cart'))
    else:
        resp = HttpResponseRedirect(reverse('sign'))

    return resp
