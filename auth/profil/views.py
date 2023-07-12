from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreatUser
from .decoretors import unauthenticated_user, allowed_users

# Create your views here.


@unauthenticated_user
def register_user(req):
    # if req.user.is_authenticated :
    #     redirect("profil")
    # else:

        if req.method == "POST":
            form = CreatUser(req.POST)
            
            if form.is_valid():
                    user = form.save()
                    username = form.cleaned_data.get('username')
                    group = Group.objects.get(name = "users")
                    user.groups.add(group)

                    print("hello",user)
                    messages.success(req,'account was created for',username)
                    return redirect('login')

            else:# can add errors
                    
                    context = {"form":form}
                    return render(req,'register.html',context)

        form = CreatUser()
        context = {"form":form}

        return render(req,'register.html',context)
        
@unauthenticated_user
def login_user(req):
    # if req.user.is_authenticated :
    #     return redirect('profil')
    # else:
        if req.method == "POST":
            username = req.POST.get("username")
            password = req.POST.get("password")

            user = authenticate(req,username = username,password = password)

            if user is not None :
                login(req,user)
                return redirect('profil')
            else:
                messages.info(req,"username or password in incorrect")

        context = {}
        return render(req,'login.html',context)


def logout_user(req):
    logout(req)
    return redirect('login')


@login_required(login_url="login")
@allowed_users(allowed_roles = ['superusers','users'])
def profil_user(req):

    context = {}
    print(req.user)
    return render(req,'profile.html',context)