from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Book
from .models import User
from .form import BookForm
from .form import UserRegister
from .login import UserLogin

import re


# Create your views here.

def homepage_view(request, *args, **kwargs):
    booksQuery = Book.objects.all()
    context = {}
    bestSeller = 0;
    culinary = 0;
    for book in booksQuery:
        if book.isBestSeller == 1:
            context["book" + str(bestSeller) ] = book
            book.title = book.title[0:50] + "..."
            book.description = book.description[0:300] + "..."
            bestSeller = bestSeller + 1
        if book.genre == "culinary":
            context["culinary" + str(culinary) ] = book
            book.title = book.title[0:50] + "..."
            book.description = book.description[0:300] + "..."
            culinary = culinary + 1;
    return render(request, "homepage.html", context)

def adminpage_view(request, *args, **kwargs):
	return render(request, "adminpage.html", {})

def checkout_view(request, *args, **kwargs):
	return render(request, "checkout.html", {})

def confirmation_view(request, *args, **kwargs):
	return render(request, "confirmation.html", {})

def details_view(request, *args, **kwargs):
    booksQuery = Book.objects.all()
    context = {}
    targetISBN = request.get_full_path()[-13:]
    for book in booksQuery:
        if book.isbn == targetISBN:
            context["book"] = book
            break
    print(dir(book));
    return render(request, "details.html", context)

@login_required(login_url = "login")
def editacct_view(request, *args, **kwargs):
	return render(request, "editacct.html", {})

def login_view(request, *args, **kwargs):
    form = UserLogin()
    if request.method =="POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            print("Valid!")
    context = {
        "form": form
    }
    return render(request, "login.html", context) 

def managebooks_view(request, *args, **kwargs):
	return render(request, "managebooks.html", {})

def newbook_view(request, *args, **kwargs):
	return render(request, "newbook.html", {})

@login_required(login_url = "login")
def orderHistory_view(request, *args, **kwargs):
	return render(request, "orderHistory.html", {})
"""
def register_view(request, *args, **kwargs):
	return render(request, "register.html", {})
"""
def search_view(request, *args, **kwargs):
	return render(request, "search.html", {})

@login_required(login_url = "login")
def verifyEmail_view(request, *args, **kwargs):
	return render(request, "verifyEmail.html", {})

@login_required(login_url = "login")
def viewCart_view(request, *args, **kwargs):
	return render(request, "viewCart.html", {})

def register_view(request, *args, **kwargs):
    form = UserRegister()
    if request.method =="POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            User.objects.create(**form.cleaned_data)
    context = {
        "form": form
    }
    return render(request, "register.html", context)

  
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

    

    
