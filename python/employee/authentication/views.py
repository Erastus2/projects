from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str


from EmployeeP import settings
from .tokens import generate_token


# Create your views here.
def home(request):
    return render(request,'authentication/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username =username):
            messages.error(request,'username already exist, Please try some other username')
            return redirect('home')

        if User.objects.filter(email =email):
            messages.error(request,'email already registered!')
            return redirect('home')
        if len(username)>10:
            messages.error(request,'username must be under 10 character')
        if pass1 != pass2:
            messages.error(request, 'Password did not match')
        if not username.isalnum():
            messages.error(request,'username must be alpha-numeric')
            return redirect('home')
        myUser = User.objects.create_user(username,email,pass1)
        myUser.first_name =firstname
        myUser.last_name =lastname
        myUser.is_active =False
        myUser.save()

        messages.success(request,'Your Account as been succefully created we have send you a confirmation email,please confirm your email in order to activate you account')

        # welcome Email:
        subject ='Welcome to code smarter with Erastus'
        message ='hello'+ myUser.first_name + '|| \n' + 'welcome to code smarter ||\n Thank you for visiting our website\n, we have also send you a confirmation email,Please confirm your email address in order to activate your account \n \n Thank you Erastus Kemboi'
        from_email = settings.EMAIL_HOST_USER
        to_list = [myUser.email]
        send_mail(subject,message,from_email,to_list, fail_silently=True)

        # email adress confirmation email
        current_site = get_current_site(request)
        email_subject ='Confirm your email & CFG -Django Login!!'
        message2 = render_to_string('email_information.html',{
            'name': myUser.first_name,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myUser.pk)),
            'token': generate_token.make_token(myUser)

        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myUser.email]
        )
        email.fail_silently =True
        email.send()
        return redirect('signin')

    return render(request,'authentication/signup.html')
def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username = username, password =pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,'authentication/index.html',{'firstname':fname})
        else:
            messages.error(request,'Bad credentials')
            return redirect('home')

    return render(request,'authentication/signin.html')
def signout(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect('home')
    # return render(request,'authentication/signout.html')





def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myUser = User.objects.get(pk= uid)
    except(TypeError,ValueError,OverflowError, User.DoesNotExist):
        myUser =None
    if myUser is not None and generate_token.check_token(myUser,token):
        myUser.is_activate = True
        myUser.save()
        login(request,myUser)
        return redirect('home')
    else:
        return render(request,'activation_failed.html')

