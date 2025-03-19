from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from .forms import ProfileForm

from .models import Profile



def userSettings(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user.profile)
        
    context = {'form': form }
    return render(request, 'users/settings.html', context)


def userProfile(request, username):
    profile =  Profile.objects.get(username=username)
    products = profile.product_set.all()
    context = {'profile': profile, 'products': products}
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


def registerUser(request):

    if request.user.is_authenticated:
        return redirect('products')


    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('products')


    context = {'form': form}
    return render(request, 'users/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('products')
