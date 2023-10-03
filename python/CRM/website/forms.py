from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Records


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50,
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
    first_name  = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    # phone = forms.CharField(required=True,
    #                         widget=forms.widgets.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}))
    address = forms.CharField(required=True,
                              widget=forms.widgets.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    city = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    zipcode = forms.CharField(required=True,
                              widget=forms.widgets.TextInput(attrs={'placeholder': 'Zipcode', 'class': 'form-control'}))

    class Meta:
        model = Records
        exclude = ("user",)
