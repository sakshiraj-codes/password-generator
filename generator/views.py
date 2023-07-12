from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    generatedpassword=''
    ls = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        ls.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        ls.extend(list('0123456789'))
    if request.GET.get('special_characters'):
        ls.extend(list('!@#$%^&*'))
    length = int(request.GET.get('length'))
    for x in range(length):
        generatedpassword+= random.choice(ls)
    return render(request, 'generator/password.html', {'password':generatedpassword})

def about(request):
    return render(request,'generator/about.html')
