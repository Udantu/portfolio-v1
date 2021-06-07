from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path('register/', user_views.register, name="toRegister"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name="toLogin"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name="toLogout"),
    path('profile/', user_views.profile, name="toProfile"),
]
