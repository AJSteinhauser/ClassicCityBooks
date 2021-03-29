from django.db import models

# Create your models here.

class Book(models.Model):
	isbn = models.CharField(max_length=15, primary_key=True)
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	description = models.TextField()
	class Meta():
		db_table = 'Books'

class User(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	phone_num = models.CharField(max_length=11)
	user_email = models.EmailField(max_length=50)
	user_pass = models.CharField(max_length=50)
	user_street = models.CharField(max_length=50)
	user_city = models.CharField(max_length=50)
	user_state = models.CharField(max_length=2)
	user_zip = models.CharField(max_length=10)
	user_card_num = models.CharField(max_length=50)
	user_card_exp = models.DateField()
	user_card_seccode = models.CharField(max_length=3)

	class Meta():
		db_table = "Users"





