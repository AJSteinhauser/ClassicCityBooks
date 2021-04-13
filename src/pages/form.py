from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'isbn',
            'author'
        ]


class UserRegister(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name*'}), label="")
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name*'}), label="")
	phone_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number*'}), label="", max_length=10, min_length=10)
	user_email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email', 'placeholder': 'Email Address*'}), label="")
	user_pass = forms.CharField(widget=forms.PasswordInput(render_value=True, attrs={'placeholder': 'Password*'}), label="", max_length=15)
	user_street = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Street'}), label="")
	user_city = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'City'}), label="")
	user_state = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'State'}), label="")
	user_zip = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}), label="", max_length=5, min_length=5)
	user_card_num = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Card Number'}), label="", max_length=16, min_length=16)
	user_card_exp = forms.DateField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Expiration Date'}), label="")
	user_card_seccode = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Security Code'}), label="", max_length=4, min_length=3)


class NewBook(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'BookTitle*'}), label="")
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Author*'}), label="")
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description*'}), label="")
    genre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Genre*'}), label="")
    isbn = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ISBN*'}), label="")
    publisher = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Publisher*'}), label="")
    publicationDate = forms.DateField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Date Published*'}), label="")
    price = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Price*'}), label="");
    cover = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'CoverImage*'}), label="");

    
class confirmRegister(forms.Form):
    user_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'ID'}), label="")
    confirm_code = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Security Code'}), label="")

class resetPass(forms.Form):
    user_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'ID'}), label="")
    user_pass = forms.CharField(widget=forms.PasswordInput(render_value=True, attrs={'placeholder': 'Password*'}), label="", max_length=15)
    confirm_code = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Security Code'}), label="")