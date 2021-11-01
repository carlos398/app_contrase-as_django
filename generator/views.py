from django.shortcuts import render
#Python
import random


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def password(request):

    characters = list('abcdefghijklmnñopqrstuvwxyz')
    characters_upper = 'abcdefghijklmnñopqrstuvwxyz'.upper()
    generated_password = ''
    
    len = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list(characters_upper))
    if request.GET.get('special'):
        characters.extend(list('-_.!"#$%&/()=?¡*]['))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    for x in range(len):
        generated_password += random.choice(characters)
    
    
    return render(request, 'password.html', {'password': generated_password})