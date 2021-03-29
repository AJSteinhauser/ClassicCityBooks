"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from pages.views import homepage_view, adminpage_view, checkout_view,confirmation_view, details_view, editacct_view, homepage_registration_confirm_view, login_view, managebooks_view, newbook_view, orderHistory_view, register_view, search_view, verifyEmail_view, viewCart_view 


urlpatterns = [
	path('', homepage_view, name = 'home'),
    path('admin/', admin.site.urls),
    path('adminpage/', adminpage_view, name='adminpage'),
    path('checkout/', checkout_view, name='checkout'),
    path('confirmation/', confirmation_view, name='confirmation'),
    path('details/', details_view, name='details'),
    path('editacct/', editacct_view, name='editacct'),
    path('homepageconfirm/', homepage_registration_confirm_view, name='homepageconfirm'),
    path('login/', login_view, name='login'),
    path('managebooks/', managebooks_view, name='managebooks'),
    path('newbook/', newbook_view, name='newbook'),
    path('orderhistory/', orderHistory_view, name='orderhistory'),
    path('register/', register_view, name='register'),
    path('search/', search_view, name='search'),
    path('verifyemail/', verifyEmail_view, name='verifyemail'),
    path('viewcart/', viewCart_view, name='viewcart'),

]
