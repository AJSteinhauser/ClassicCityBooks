from django.db import models

# Create your models here.

class Book(models.Model):
	isbn = models.CharField(max_length=15, primary_key=True)
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	description = models.TextField()
	cover = models.TextField(null = True)
	class Meta():
		db_table = 'Books'

class User(models.Model):
	first_name = models.CharField(max_length=25, null=True)
	last_name = models.CharField(max_length=25, null=True)
	phone_num = models.CharField(max_length=11, null=True)
	user_email = models.EmailField(max_length=50, primary_key=True)
	user_pass = models.CharField(max_length=50, null=True)
	user_street = models.CharField(max_length=50, null=True)
	user_city = models.CharField(max_length=50, null=True)
	user_state = models.CharField(max_length=2, null=True)
	user_zip = models.CharField(max_length=10, null=True)
	user_card_num = models.CharField(max_length=50, null=True)
	user_card_exp = models.DateField(null=True)
	user_card_seccode = models.CharField(max_length=3, null=True)

	class Meta():
		db_table = "Users"





