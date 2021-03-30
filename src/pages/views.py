from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required

=======
from .models import Book
from .models import User
from .form import BookForm
from .form import UserRegister
>>>>>>> b72a9749c3c8dd4ac1819e5cd237eae4088c0317

# Create your views here.

def homepage_view(request, *args, **kwargs):
	return render(request, "homepage.html", {})

def adminpage_view(request, *args, **kwargs):
	return render(request, "adminpage.html", {})

def confirmation_view(request, *args, **kwargs):
	return render(request, "confirmation.html", {})

def details_view(request, *args, **kwargs):
	return render(request, "details.html", {})

def homepage_registration_confirm_view(request, *args, **kwargs):
	return render(request, "homepage_registration_confirm.html", {})

def login_view(request, *args, **kwargs):
	return render(request, "login.html", {})  

def managebooks_view(request, *args, **kwargs):
	return render(request, "managebooks.html", {})

def newbook_view(request, *args, **kwargs):
	return render(request, "newbook.html", {})

def orderHistory_view(request, *args, **kwargs):
	return render(request, "orderHistory.html", {})

def register_view(request, *args, **kwargs):
	return render(request, "register.html", {})

def search_view(request, *args, **kwargs):
	return render(request, "search.html", {})

def verifyEmail_view(request, *args, **kwargs):
	return render(request, "verifyEmail.html", {})

def viewCart_view(request, *args, **kwargs):
	return render(request, "viewCart.html", {})

def test_view(request, *args, **kwargs):
    form = UserRegister()
    if request.method =="POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
        
    context = {
        "form": form
    }
    return render(request, "test.html", context)
  
"""  
def test_view(request, *args, **kwargs):
    context = {}
    return render(request, "test.html", context)
"""

"""
def test_view(request, *args, **kwargs):
    #obj = Book.objects.get(isbn=123456789)
    #context = {
    #    'object': obj
    #}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "test.html", context)
"""

    

    
