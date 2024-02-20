from django.shortcuts import render

# Create your views here.

def LogIn(request):
    return render(request, 'accounts/login.html')