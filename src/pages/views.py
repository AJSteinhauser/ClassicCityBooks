from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Book
from .models import User
from .form import BookForm
from .form import UserRegister
from .login import UserLogin
from .email import emailSelf
from .email import recoverEmail


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

def navbar_view(request, *args, **kwargs):
	return render(request, "navbar.html", {})

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
    if request.session.has_key('user_id'):
        user = User.objects.get(user_id=request.session.get('user_id'))
        password = user.user_pass
        form = UserRegister(initial={'first_name': user.first_name, 
        'last_name': user.last_name, 'phone_num': user.phone_num,
        'user_email': user.user_email, 'user_pass': password, #NOT WORKING
        'user_street': user.user_street, 'user_city': user.user_city,
        'user_state': user.user_state, 'user_zip': user.user_zip,
        'user_card_num': user.user_card_num, 'user_card_exp': user.user_card_exp,
        'user_card_seccode': user.user_card_seccode})
        form.fields['user_email'].widget.attrs['readonly'] = True
        if request.method =="POST":
            form = UserRegister(request.POST)
            if form.is_valid():
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.user_pass = form.cleaned_data['user_pass']
                user.phone_num = form.cleaned_data['phone_num']
                user.user_street = form.cleaned_data['user_street']
                user.user_city= form.cleaned_data['user_city']
                user.user_state= form.cleaned_data['user_state']
                user.user_zip= form.cleaned_data['user_zip']
                user.user_card_num= form.cleaned_data['user_card_num']
                user.user_card_exp= form.cleaned_data['user_card_exp']
                user.user_card_seccode= form.cleaned_data['user_card_seccode']
                user.save()
                messages.error(request, "You're changes have been saved!")
                return render(request, "logout.html", {})
        context = {
            "form": form
        }
    else:
        context = {}
    return render(request, "editacct.html", context)

def login_view(request, *args, **kwargs):
    if request.session.has_key('user_id'):
        print("TEST")
        messages.error(request, "You're already logged in")
        #return render(request, "details.html", context) 
    form = UserLogin()
    if request.method =="POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            id = form.cleaned_data["user_id"]
            email = form.cleaned_data["user_email"]
            user_password = form.cleaned_data["user_pass"]
            if id == "" and email=="":
                messages.error(request, "Please enter an ID or an Email")
            elif id != "":
                try:
                    obj = User.objects.get(user_id=id)
                    if user_password != obj.user_pass:
                        messages.error(request, "Either your ID or Password is incorrect")
                    else:
                        request.session['user_id'] = id
                        messages.info(request, "You have been logged in!")
                except: 
                    messages.error(request, "That ID does not exist")
            else:
                try:
                    obj = User.objects.get(user_email=email)
                    if user_password != obj.user_pass:
                        messages.error(request, "Either your Email or Password is incorrect")
                    else:
                        id = obj.user_id
                        request.session['user_id'] = id
                        messages.info(request, "You have been logged in!")
                except: 
                    messages.error(request, "That email does not exist")
    context = {
        "form": form
    }
    return render(request, "login.html", context)
    
def logout_view(request, *args, **kwargs):
    try:
        del request.session['user_id']
        messages.error(request, "You have been logged out!")
    except:
        messages.error(request, "You are not logged in!")
    return render(request, "logout.html", {})

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

#@login_required(login_url = "login")
def verifyEmail_view(request, *args, **kwargs):
	return render(request, "verifyEmail.html", {})

@login_required(login_url = "login")
def viewCart_view(request, *args, **kwargs):
	return render(request, "viewCart.html", {})
    
def recover_view(request, *args, **kwargs):
    form = UserLogin()
    if request.method =="POST":
        form = UserLogin(request.POST)
        if not form.is_valid():
            id = form.cleaned_data["user_id"]
            email = form.cleaned_data["user_email"]
            if id == "" and email == "":
                messages.error(request, "Please enter an ID or an Email")
            elif id != "" and email != "":
                messages.error(request, "Please enter either the ID or the Email, not both")
            else: 
                id = form.cleaned_data["user_id"]
                email = form.cleaned_data["user_email"]
                if email == "":
                    try:
                        obj = User.objects.get(user_id=id)
                        email = obj.user_email
                        password = obj.user_pass
                        recoverEmail(email, password)
                        messages.error(request, "A recovery email has been sent to the email associated with that account")
                        return render(request, "logout.html", {})
                    except:
                        messages.error(request, "There is no account with that ID")
                else:
                    try:
                        obj = User.objects.get(user_email=email)
                        password = obj.user_pass
                        recoverEmail(email, password)
                        messages.error(request, "A recovery email has been sent to the email associated with that account")
                        return render(request, "logout.html", {})
                    except:
                        messages.error(request, "There is no account with that Email")
            
    
    context = {
        "form": form
    }
    return render(request, "recover.html", context)

def register_view(request, *args, **kwargs):
    form = UserRegister()
    if request.method =="POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            entered_email = form.cleaned_data["user_email"]
            try:
                obj = User.objects.get(user_email=entered_email)
                messages.error(request, "There is already an account with that email!")
            except:
                User.objects.create(**form.cleaned_data)
                obj = User.objects.get(user_email=entered_email)
                emailSelf(entered_email, obj.user_id)
                messages.info(request, "A unique account ID has been sent to your email. This can be used as an alrternative to email and password login. We look forward to your business!")
                return render(request, "logout.html", {})
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

    

    
