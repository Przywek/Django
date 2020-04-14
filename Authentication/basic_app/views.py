from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not Active')
        else:
            print('someone tried login and filed')
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request,'basic_app/login.html',{})
# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    registered = False
    if request.method == "POST":
        print('start')
        print(request.POST)
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            print('valid')
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            print('uzytkownik jest')
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            print('profil jest')
            registered = True
        else:
            print(UserForm.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'basic_app/registration.html',
                  {'user_form':user_form,'profile_form':profile_form,'registered':registered})
