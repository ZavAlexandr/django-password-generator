import random
from django.shortcuts import render


def home_page(request):
    return render(request, 'generator/home.html')


def password_page(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 7))

    your_password = ''
    for x in range(length):
        your_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': your_password})
