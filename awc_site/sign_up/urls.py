from django.conf.urls import url
from django.urls import path
from sign_up import views
from sign_up.views import register
from django.contrib.auth import views as auth_view

#app_name = 'sign_up'

urlpatterns = [
    path('register', register, name='register'),
    path('login/', auth_view.LoginView.as_view(), name='login'),

]
