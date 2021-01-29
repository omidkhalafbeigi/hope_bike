from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
    cookies = request.COOKIES
    is_logged, message = sign_checker(cookies)

    response = render(request, template_name='app/index.html', context={'message': message})

    return response


def bikes(request):
    cookies = request.COOKIES
    is_logged, message = sign_checker(cookies)

    response = render(request, template_name='app/bikes.html', context={'message': message})

    return response


def about(request):
    cookies = request.COOKIES
    is_logged, message = sign_checker(cookies)

    response = render(request, template_name='app/AboutUs.html', context={'message': message})

    return response

