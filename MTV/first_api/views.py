from django.shortcuts import render
from django.http import HttpResponse
from first_api.models import Users
from first_api.forms import User_form
# Create your views here.
def index(request):
    return HttpResponse("<h1>WELCOME!<h1> <em> Go to /users to see the list of information <em>")
def indhtml(request):
    my_dict = {'insert_me':"hello it's me you looking for"}
    return render(request,'first_app/index.html',context=my_dict)
def help(request):
    my_dict = {'help_insert':"Hi i'm helping"}
    return render(request,'first_app/help.html',context=my_dict)

def users(request):
    user_list = Users.objects.order_by('first_name')
    my_dict = {'users_info':user_list}
    return render(request,'first_app/users.html',context=my_dict)

def signin_view(request):
    form = User_form()
    if request.method == 'POST':
        form = User_form(request.POST)
        if form.is_valid():
            # DO Something Code
            print("VAlidation succes")
            print(form.cleaned_data)
            new_user = form.save()
    return render(request,'first_app/signin.html',{'form':form})