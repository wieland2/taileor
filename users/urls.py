from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('account/', views.userAccount, name="account"),
    path('<str:username>/', views.userProfile, name="profile"),
]
