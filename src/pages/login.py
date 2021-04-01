from django import forms

class UserLogin(forms.Form):
    user_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Account ID'}), label="", required=False)
    user_email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email', 'placeholder': 'Email Address'}), label="", required=False)
    user_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label="")

def logout(request):
   try:
      del request.session['username']
   except:
      pass