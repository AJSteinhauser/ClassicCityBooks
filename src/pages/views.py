from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage_view(request, *args, **kwargs):
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