from django.contrib.auth.forms import UserCreationForm;

from django.contrib.auth.models import User;
from django import forms
from  .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __int__(self):
        super(SignUpForm, self).__init__()
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'


# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}),label="")
    last_name=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}),label="")
    email=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}),label="")
    address=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}),label="")
    city=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}),label="")
    state=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}),label="")
    zipcode=forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}),label="")

    class Meta:
        model= Record
        exclude= ("user",)