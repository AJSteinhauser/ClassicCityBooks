from django.db import models


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=15)
    title = models.CharField(max_length=150, blank=True, null=True)
    author = models.CharField(max_length=50)
    description = models.TextField()
    cover = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    isbestseller = models.IntegerField(db_column='isBestSeller', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Books'


class User(models.Model):
    user_id = models.AutoField(max_length=50, primary_key=True)
    user_email = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    phone_num = models.CharField(max_length=11, blank=True, null=True)
    user_card_exp = models.DateField(blank=True, null=True)
    user_card_num = models.CharField(max_length=50, blank=True, null=True)
    user_card_seccode = models.CharField(max_length=3, blank=True, null=True)
    user_city = models.CharField(max_length=50, blank=True, null=True)
    user_state = models.CharField(max_length=2, blank=True, null=True)
    user_street = models.CharField(max_length=50, blank=True, null=True)
    user_zip = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Users'





