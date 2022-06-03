from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserLoginForm
from . import views

urlpatterns = [
    path('user-register/', views.user_register, name='user-register'),
    path('login/', LoginView.as_view(template_name='users/login.html',
                                     authentication_form=UserLoginForm),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),
]
