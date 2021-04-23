from django.db import models
import json
from django_cryptography.fields import encrypt


class Promotions(models.Model):
    start_date = models.DateField(blank=True, null=True);
    end_date = models.DateField(blank=True, null=True);
    isActive = models.BooleanField(default=False);
    promocode = models.CharField(max_length=15);
    percent = models.PositiveIntegerField(blank=True, null=True)

class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=15)
    title = models.CharField(max_length=150, blank=True, null=True)
    author = models.CharField(max_length=50)
    description = models.TextField()
    cover = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    isBestSeller = models.IntegerField(db_column='isBestSeller', blank=True, null=True)  # Field name made lowercase.
    publicationDate = models.DateField(blank=True, null=True)
    publisher = models.CharField(max_length=100)
    price = models.FloatField();
    class Meta:
        managed = True
        db_table = 'Books'

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    phone_num = models.PositiveIntegerField(blank=True, null=True)
    cart = models.CharField(max_length=9000000000000);
    user_card_exp = models.CharField(max_length=150, blank=True, null=True)
    user_card_num = models.CharField(max_length=50, blank=True, null=True)
    user_card_seccode = models.CharField(max_length=3, blank=True, null=True)
    user_city = models.CharField(max_length=50, blank=True, null=True)
    user_state = models.CharField(max_length=2, blank=True, null=True)
    user_street = models.CharField(max_length=50, blank=True, null=True)
    user_zip = models.CharField(max_length=11, blank=True, null=True)
    confirm_code = models.PositiveIntegerField(null=True)
    confirmed = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False);
    isSubscribed = models.BooleanField(default=False);
    isSuspended = models.BooleanField(default=False);

    class Meta:
        managed = True
        db_table = 'Users'

class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    promocode = models.CharField(max_length=255, blank=True, null=True)
    percent = models.FloatField(null=True)
    isActive = models.BooleanField(default=False);
    
    class Meta:
        managed = True
        db_table = 'Promotions'

