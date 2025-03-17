from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .models import Profile



def userProfile(request, username):
    profile =  Profile.objects.get(username=username)
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('products')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Profile.objects.get(username=username)
        except:
            print("Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products')
        else:
            print("USername OR password is incorrect")

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    return redirect('products')
