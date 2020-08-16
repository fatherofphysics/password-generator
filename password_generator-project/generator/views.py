from django.shortcuts import render
import random

# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(requesst):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if requesst.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if requesst.GET.get('number'):
        characters.extend(list('0123456789'))
        
    if requesst.GET.get('special'):
        characters.extend(list("!~@#$%^'&*()_+=/\|<>.,]["))
        
    length = int(requesst.GET.get('length',12))
    
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
        
    return render(requesst, 'password.html', {'password':thepassword})