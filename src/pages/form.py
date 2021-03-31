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
	user_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password*'}), label="")
	user_street = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Street'}), label="")
	user_city = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'City'}), label="")
	user_state = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'State'}), label="")
	user_zip = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}), label="")
	user_card_num = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Card Number'}), label="")
	user_card_exp = forms.DateField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Expiration Date'}), label="")
	user_card_seccode = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Security Code'}), label="")
    
    
    #first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_field'}),label="")
    