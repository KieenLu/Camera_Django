from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return HttpResponse('Tài khoản của bạn là')

