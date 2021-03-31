from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import User
from .form import BookForm
from .form import UserRegister

# Create your views here.

def homepage_view(request, *args, **kwargs):
    '''
    booksQuery = Book.objects.all()
    context = {};
    iterator = 0;
    for book in booksQuery:
        if iterator > 16:
            break
        context["Book" + iterator ] = book;
        iterator++;
'''
    return render(request, "homepage.html", {})





def adminpage_view(request, *args, **kwargs):
	return render(request, "adminpage.html", {})

def checkout_view(request, *args, **kwargs):
	return render(request, "checkout.html", {})

def confirmation_view(request, *args, **kwargs):
	return render(request, "confirmation.html", {})

def details_view(request, *args, **kwargs):
	return render(request, "details.html", {})

def editacct_view(request, *args, **kwargs):
	return render(request, "editacct.html", {})

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

def test2_view(request, *args, **kwargs):
    booksQuery = Book.objects.all()
    context = {}
    iterator = 0
    for book in booksQuery:
        if iterator > 16:
            break
        context["book" + str(iterator) ] = book
        iterator = iterator + 1
    return render(request, "test2.html", context)


  
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

    

    
