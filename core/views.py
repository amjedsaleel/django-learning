from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from . models import *


def index(request):
    user = User.objects.get(id=1).phone.user
    user_phone = User.objects.get(id=1).phone
    details = User.objects.get(id=1).phone.id

    print(user)
    print(user_phone)
    print(details)
    # print('\n')

    user1 = Phone.objects.get(id=1).user
    user_phone1 = Phone.objects.get(id=1).user.phone
    details1 = Phone.objects.get(id=1).user.id

    print(user1)
    print(user_phone1)
    print(details1)

    return HttpResponse('Hello...')

