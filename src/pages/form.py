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
	phone_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number*'}), label="")
	user_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address*'}), label="")
	user_pass = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password*'}), label="")
	user_street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Street'}), label="")
	user_city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}), label="")
	user_state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'State'}), label="")
	user_zip = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}), label="")
	user_card_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Card Number'}), label="")
	user_card_exp = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Expiration Date'}), label="")
	user_card_seccode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Security Code'}), label="")
    
    
    #first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_field'}),label="")
    