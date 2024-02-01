from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Record
from django import forms
from django.forms.widgets import TextInput,PasswordInput


#register
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2"]
    
#login
class LoginForm(AuthenticationForm):
    username =forms.CharField(widget=TextInput)
    password=forms.CharField(widget=PasswordInput)
    
# create record 
class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=["first_name","last_name","email","phone"]
        
#upload record
class UploadForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=["first_name","last_name","email","phone"]
        
#update Record

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=["first_name","last_name","email","phone"]
    
    
    