from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.templatetags.static import static
from .models import Book
from .models import User
from .models import Promotion
from .form import BookForm
from .form import UserRegister
from .form import NewBook
from .form import searchForm
from .login import UserLogin
from .email import emailSelf
from .email import recoverEmail
from .form import confirmRegister
from .form import resetPass
from random import randint
from .email import accountChange
from .email import promoEmail
from django_cryptography.fields import encrypt
from cryptography.fernet import Fernet
import os
from django.conf import settings
import re
import datetime
from .form import newpromotion
from django.http import HttpResponseRedirect
from .form import userStatus
import datetime
import json
# Create your views here.

def checkSuspendedStatus(request, *args, **kwargs):
    if request.session.has_key('user_id'):
        del request.session['user_id']
        user = User.objects.get(user_id=request.session.get('user_id'))
        return user.isSuspended
    return False

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
    if(checkSuspendedStatus(request, *args, **kwargs)):
        if request.session.has_key('user_id'):
            del request.session['user_id']
        if request.session.has_key('isAdmin'):
            del request.session['isAdmin']
    return render(request, "homepage.html", context)

def adminpage_view(request, *args, **kwargs):
    if checkAdminStatus(request, *args, **kwargs):
	    return render(request, "adminpage.html", {})
    return homepage_view(request, *args, **kwargs);

def checkout_view(request, *args, **kwargs):
	return render(request, "checkout.html", {})

def navbar_view(request, *args, **kwargs):
	return render(request, "navbar.html", {})

def confirmation_view(request, *args, **kwargs):
    form = confirmRegister()
    if request.method =="POST":
        form = confirmRegister(request.POST)
        if form.is_valid():
            id = form.cleaned_data["user_id"]
            confirm_code = form.cleaned_data["confirm_code"]
            try:
                obj = User.objects.get(user_id=id)
                if obj.user_id == id and obj.confirm_code == confirm_code:
                    messages.info(request, "Your account is confirmed. You can login now!")
                    obj.confirmed = True
                    obj.save()
                    return render(request, "logout.html", {})
                else:
                    messages.info(request, "Either the ID or the security code is incorrect")
            except:
                messages.info(request, "No account exists with that ID!")
    context = {
        "form": form
    }
    return render(request, "confirmation.html", context)

def resetpass_view(request, *args, **kwargs):
    form = resetPass()
    if request.method =="POST":
        form = resetPass(request.POST)
        if form.is_valid():
            id = form.cleaned_data["user_id"]
            confirm_code = form.cleaned_data["confirm_code"]
            try:
                obj = User.objects.get(user_id=id)
                if obj.user_id == id and obj.confirm_code == confirm_code:
                    accountChange(obj.user_email)
                    messages.info(request, "Your password has been reset!")
                    key = open(os.path.join(settings.BASE_DIR, 'secret.key')).read()
                    f = Fernet(key)
                    obj.user_pass = f.encrypt((form.cleaned_data['user_pass']).encode('utf-8'))
                    #obj.user_pass = form.cleaned_data["user_pass"]
                    obj.save()
                    return render(request, "logout.html", {})
                else:
                    messages.info(request, "Either the ID or the security code is incorrect")
            except:
                messages.info(request, "No account exists with that ID!")
    context = {
        "form": form
    }
    return render(request, "resetpass.html", context)

def addtocart(cart, book):
    found = False;
    for item in cart:
        if book.title == cart[item]["book_title"]:
            if int(cart[item]["quantity"]) < 10:
                cart[item]["quantity"] = str(int(cart[item]["quantity"]) + 1);
            found = True;
            break;
    if not found:
        cart[str(len(cart)+1)] = {"book_title" : book.title, 
                    "quantity" : "1",
                    "price" : book.price
                    }
    return cart;
  


def details_view(request, *args, **kwargs):
    booksQuery = Book.objects.all()
    context = {}
    mainbook = None;
    targetISBN = request.get_full_path()[-13:]
    for book in booksQuery:
        if book.isbn == targetISBN:
            context["book"] = book
            mainbook = book;
            break
    if request.method =="POST":
        if request.session.has_key('user_id'):
            user = User.objects.get(user_id=request.session.get('user_id'))
            tmpcart = user.cart or "{}"
            cart = json.loads(tmpcart);
            user.cart = json.dumps(addtocart(cart,mainbook))
            user.save();
            return viewCart_view(request, *args, **kwargs)
        else:
            return render(request, "details.html", context)
    return render(request, "details.html", context)


def unencrypt(string):
    key = open(os.path.join(settings.BASE_DIR, 'secret.key')).read()
    f = Fernet(key)
    string = string[2:len(string)-1]
    string = string.encode()
    string = f.decrypt(string)
    string = string.decode()
    return string
    

def editacct_view(request, *args, **kwargs):
    if request.session.has_key('user_id'):
        user = User.objects.get(user_id=request.session.get('user_id'))
        password = unencrypt(user.user_pass)
        if user.user_card_num != "":
            card_num = unencrypt(user.user_card_num)
        else:
            card_num = ""
        if user.user_card_seccode != "":
            card_seccode = unencrypt(user.user_card_seccode)
        else:
            card_seccode = ""
        if user.user_card_exp != None:
            card_exp = unencrypt(user.user_card_exp)
        else:
            card_exp = ""
        form = UserRegister(initial={'first_name': user.first_name, 
        'last_name': user.last_name, 'phone_num': user.phone_num,
        'user_email': user.user_email, 'user_pass': password, 
        'user_street': user.user_street, 'user_city': user.user_city,
        'user_state': user.user_state, 'user_zip': user.user_zip,
        'user_card_num': card_num, 'user_card_exp': card_exp,
        'user_card_seccode': card_seccode, 'isSubscribed': user.isSubscribed})
        form.fields['user_email'].widget.attrs['readonly'] = True
        if request.method =="POST":
            form = UserRegister(request.POST)
            if form.is_valid():
                key = open(os.path.join(settings.BASE_DIR, 'secret.key')).read()
                f = Fernet(key)
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                #user.user_pass = form.cleaned_data['user_pass']
                user.user_pass = f.encrypt((form.cleaned_data['user_pass']).encode('utf-8'))
                user.phone_num = form.cleaned_data['phone_num']
                user.user_street = form.cleaned_data['user_street']
                user.user_city= form.cleaned_data['user_city']
                user.user_state= form.cleaned_data['user_state']
                user.user_zip= form.cleaned_data['user_zip']
                user.user_card_num= f.encrypt((form.cleaned_data['user_card_num']).encode('utf-8'))
                date = form.cleaned_data['user_card_exp']
                if date != None:
                    date = date.strftime('%m/%d/%Y')
                    user.user_card_exp= f.encrypt((date).encode('utf-8'))
                else:
                    user.user_card_exp = None
                user.user_card_seccode= f.encrypt((form.cleaned_data['user_card_seccode']).encode('utf-8'))
                user.isSubscribed = form.cleaned_data['isSubscribed']
                user.save()
                accountChange(user.user_email)
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
            
            key = open(os.path.join(settings.BASE_DIR, 'secret.key')).read()
            f = Fernet(key)
            user_password = f.encrypt((user_password).encode())
            user_password = f.decrypt(user_password)
            user_password = user_password.decode()
            
            if id == "" and email=="":
                messages.error(request, "Please enter an ID or an Email")
            elif id != "":
                try:
                    obj = User.objects.get(user_id=id)
                    data_pass = obj.user_pass[2:]
                    data_pass = obj.user_pass[2:]
                    data_pass = data_pass[:len(data_pass)-1]
                    data_pass = data_pass.encode()
                    data_pass = f.decrypt(data_pass)
                    data_pass = data_pass.decode()
                    if user_password != data_pass:
                        messages.error(request, "Either your ID or Password is incorrect")
                    else:
                        if obj.confirmed == False:
                            messages.info(request, "You need to confirm your account! Check your email")
                        elif obj.isSuspended == True:
                            messages.info(request, "Your account is suspended! Please contact us if you believe this was an accident.")
                        else:
                            request.session['user_id'] = id
                            request.session['isAdmin'] = obj.isAdmin
                            messages.info(request, "You are logged in!")
                except: 
                    messages.error(request, "That ID does not exist")
            else:
                try:
                    obj = User.objects.get(user_email=email)
                    data_pass = obj.user_pass[2:]
                    data_pass = obj.user_pass[2:]
                    data_pass = data_pass[:len(data_pass)-1]
                    data_pass = data_pass.encode()
                    data_pass = f.decrypt(data_pass)
                    data_pass = data_pass.decode()
                    if user_password != data_pass:
                        messages.error(request, "Either your Email or Password is incorrect")
                    else:
                        if obj.confirmed == False:
                            messages.info(request, "You need to confirm your account! Check your email")
                        elif obj.isSuspended == True:
                            messages.info(request, "Your account is suspended! Please contact us if you believe this was an accident.")
                        else:
                            id = obj.user_id
                            request.session['user_id'] = id
                            request.session['isAdmin'] = obj.isAdmin
                            messages.info(request, "You are logged in!")
                except: 
                    messages.error(request, "That email does not exist")
    context = {
        "form": form
    }
    return render(request, "login.html", context)
    
def logout_view(request, *args, **kwargs):
    try:
        del request.session['user_id']
        messages.error(request, "You are logged out!")
    except:
        messages.error(request, "You are not logged in!")
    return render(request, "logout.html", {})

def managebooks_view(request, *args, **kwargs):
    if checkAdminStatus(request, *args, **kwargs):
	    return render(request, "managebooks.html", {})
    return homepage_view(request, *args, **kwargs);


@login_required(login_url = "login")
def orderHistory_view(request, *args, **kwargs):
	return render(request, "orderHistory.html", {})
"""
def register_view(request, *args, **kwargs):
	return render(request, "register.html", {})
"""
def search_view(request, *args, **kwargs):
    form = searchForm()
    if request.method =="POST":
        form = searchForm(request.POST)
    context = {
        "form": form
    }
    return render(request, "search.html", context)

#@login_required(login_url = "login")
def verifyEmail_view(request, *args, **kwargs):
	return render(request, "verifyEmail.html", {})

def viewCart_view(request, *args, **kwargs):
    context = {};
    if request.session.has_key('user_id'):
        
        user = User.objects.get(user_id=request.session.get('user_id'))
        tmp = user.cart or "{}"
        cart = json.loads(tmp)
        if request.method =="POST":
            for key, value in request.POST.items():
                for item in cart:
                    if cart[item]["book_title"] == key:
                        if value != str(0):
                            cart[item]["quantity"] = str(value);
                            break;
                        else:
                            print("DELETE TIME BOYS\n")
                            del cart[item];
                            break;

            user.cart = json.dumps(cart)
            user.save();
        loop = {}
        total = 0;
        for item in cart:
            total = total + cart[item]["price"] * int(cart[item]["quantity"]);
        for i in range(0,11):
            loop[str(i)] = str(i);

        context = {"cart" : cart, "loop": loop, "total":total}
    return render(request, "viewCart.html", context)

def checkAdminStatus(request, *args, **kwargs):
    if request.session.has_key('user_id'):
        user = User.objects.get(user_id=request.session.get('user_id'))
        return user.isAdmin
    return False

def checkSuspendedStatus(request, *args, **kwargs):
    if request.session.has_key('user_id'):
        user = User.objects.get(user_id=request.session.get('user_id'))
        print(user.isSuspended)
        return user.isSuspended
    return False
    
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
                        confirm_code = randint(100000,999999)
                        obj.confirm_code = confirm_code
                        obj.save()
                        recoverEmail(email, confirm_code, id)
                        messages.error(request, "A recovery email has been sent to the email associated with that account")
                        return render(request, "logout.html", {})
                    except:
                        messages.error(request, "There is no account with that ID")
                else:
                    try:
                        obj = User.objects.get(user_email=email)
                        id = obj.user_id
                        password = obj.user_pass
                        confirm_code = randint(100000,999999)
                        obj.confirm_code = confirm_code
                        obj.save()
                        recoverEmail(email, confirm_code, id)
                        messages.error(request, "A recovery email has been sent to the email associated with that account")
                        return render(request, "logout.html", {})
                    except:
                        messages.error(request, "There is no account with that Email")
            
    
    context = {
        "form": form
    }
    return render(request, "recover.html", context)


def newbook_view(request, *args, **kwargs):  
    context = {};
    if checkAdminStatus(request, *args, **kwargs):
        form = NewBook(initial={});
        context = {"form": form}
        if request.method =="POST":
            form = NewBook(request.POST)
            
            if form.is_valid():
                context = {"form": form}
                isbn_entered = form.cleaned_data["isbn"];
                try:
                    obj = Book.objects.get(isbn=isbn_entered);#Errors if book does not exist
                    messages.error(request, "This book already exists");
                    return render(request, "newbook.html", context) 
                except:
                    try:
                        Book.objects.create(**form.cleaned_data)
                        obj = Book.objects.get(isbn=isbn_entered)
                        obj.title = form.cleaned_data['title']
                        obj.author = form.cleaned_data['author']
                        obj.genre = form.cleaned_data['genre']
                        obj.description = form.cleaned_data['description']
                        obj.publicationDate = form.cleaned_data['publicationDate'];
                        obj.price = float(form.cleaned_data['price']);
                        obj.cover = "assets/" + form.cleaned_data['cover'];
                        obj.save()
                        messages.error(request, "Changes saved")
                        return render(request, "newbook.html", context)
                    except:
                        messages.error(request, "There is a problem with some of the data input")
                        return render(request, "newbook.html", context)


    else:
        return homepage_view(request, *args, **kwargs);
    return render(request, "newbook.html", context)

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
                confirm_code = randint(100000,999999)
                obj.confirm_code = confirm_code
                
                key = open(os.path.join(settings.BASE_DIR, 'secret.key')).read()
                f = Fernet(key)
                if form.cleaned_data["user_pass"] != "":
                    obj.user_pass = f.encrypt((obj.user_pass).encode('utf-8'))
                if form.cleaned_data["user_card_num"] != "":
                    obj.user_card_num = f.encrypt((obj.user_card_num).encode('utf-8'))
                if form.cleaned_data["user_card_exp"] != None:
                    print(form.cleaned_data["user_card_exp"])
                    obj.user_card_exp = f.encrypt((obj.user_card_exp).encode('utf-8'))
                if form.cleaned_data["user_card_seccode"] != None:
                    obj.user_card_seccode = f.encrypt((obj.user_card_seccode).encode('utf-8'))
                obj.save()
                emailSelf(entered_email, obj.user_id, confirm_code)
                messages.info(request, "A unique account ID has been sent to your email. This can be used as an alrternative to email and password login. We look forward to your business!")
                return render(request, "logout.html", {})
    context = {
        "form": form
    }
    return render(request, "register.html", context)

def promotions_view(request, *args, **kwargs):
    if not checkAdminStatus(request, *args, **kwargs):
        return homepage_view(request, *args, **kwargs);
    return render(request, "promotions.html", {})

def newpromotion_view(request, *args, **kwargs):
    if not checkAdminStatus(request, *args, **kwargs):
        return homepage_view(request, *args, **kwargs);
    form = newpromotion()
    if request.method =="POST":
        form = newpromotion(request.POST)
        if form.is_valid():
            try:
                obj = Promotion.objects.get(promocode=form.cleaned_data["promocode"])
                messages.error(request, "There is already a promotion with that promo code!")
            except:
                if (form.cleaned_data["percent"] > 100 or form.cleaned_data["percent"] < 0):
                    messages.error(request, "Please enter a valid percent!")
                elif(form.cleaned_data["start_date"] < datetime.date.today()):
                    messages.error(request, "Start dates must begin either today or later")
                    return HttpResponseRedirect(".") 
                elif(not(form.cleaned_data["start_date"] < form.cleaned_data["end_date"])):
                    messages.error(request, "Start dates must begin before expiration date")
                    return HttpResponseRedirect(".")                 
                else:
                    Promotion.objects.create(**form.cleaned_data)
                    obj = Promotion.objects.get(promocode=form.cleaned_data["promocode"])
                    obj.isActive = False
                    obj.save()
                    button = request.POST.get("saveandsub")
                    if (not button):
                        print(form.cleaned_data["start_date"].strftime('%m/%d/%Y'))
                        messages.error(request, "Promotion Saved!")
                        return HttpResponseRedirect(".")
                    else:
                        emailAllUsers(
                        str(form.cleaned_data["promocode"]), 
                        str(form.cleaned_data["percent"]),
                        form.cleaned_data["start_date"].strftime('%m/%d/%Y'),
                        form.cleaned_data["end_date"].strftime('%m/%d/%Y'))
                        obj.isActive = True
                        obj.save()
                        messages.error(request, "Promotion Saved and Sent to the Users!")
                    print(request.POST)
                    return HttpResponseRedirect(".")
    context = {
        "form": form
    }
    return render(request, "newpromotion.html", context)

    
def emailAllUsers(promocode, percentage, start, end):
    subbedUsers = User.objects.filter(isSubscribed=True)
    for user in subbedUsers:
        promoEmail(
        user.user_email,
        promocode,
        percentage,
        start,
        end)
                    
def viewpromotions_view(request, *args, **kwargs):
    promotionsQuery = Promotion.objects.all()
    context = {
        "promotion_list": promotionsQuery
    }
    for promotion in promotionsQuery:
        context["promotion"] = promotion;
    if request.method =="POST":
        promo = Promotion.objects.get(id=request.POST.get("name"))
        emailAllUsers(str(promo.promocode), str(promo.percent), promo.start_date.strftime('%m/%d/%Y'), promo.end_date.strftime('%m/%d/%Y'))
        promo.isActive = 1
        promo.save()
        return HttpResponseRedirect(".")
    return render(request, "viewpromotions.html", context)
    


def manageusers_view(request, *args, **kwargs):
    if not checkAdminStatus(request, *args, **kwargs):
        return homepage_view(request, *args, **kwargs);

    return render(request, "manageusers.html", {})

def suspenduser_view(request, *args, **kwargs):
    if not checkAdminStatus(request, *args, **kwargs):
        return homepage_view(request, *args, **kwargs);
    form = userStatus()
    if request.method == "POST":
        form = userStatus(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(user_id=form.cleaned_data["user_id"])
                if (user.isSuspended == 1):
                    messages.error(request, "That user is already suspended!")
                else:
                    user.isSuspended = 1
                    user.save()
                    messages.error(request, "The user is suspended!")
                    return HttpResponseRedirect('.')
            except:
                messages.error(request, "There is not a user with that ID")

    context = {
        "form": form
    }

    return render(request, "suspenduser.html", context)

def unsuspend_view(request, *args, **kwargs):
    if not checkAdminStatus(request, *args, **kwargs):
        return homepage_view(request, *args, **kwargs);
    form = userStatus()
    if request.method == "POST":
        form = userStatus(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(user_id=form.cleaned_data["user_id"])
                if (user.isSuspended == 0):
                    messages.error(request, "That user is already unsuspended!")
                else:
                    user.isSuspended = 0
                    user.save()
                    messages.error(request, "The user is unsuspended!")
                    return HttpResponseRedirect('.')
            except:
                messages.error(request, "There is not a user with that ID")

    context = {
        "form": form
    }
    return render(request, "unsuspend.html", context)


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

    

    
