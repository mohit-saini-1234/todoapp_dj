from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path as url
from todo_user.views import UserAuth , UserRegister , UserProfile ,UpdateUserView, ChangePasswordView ,DeleteUserView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', UserAuth.as_view()),
    url(r'^profile/$', UserProfile.as_view()),
    url(r'^register/$', UserRegister.as_view()),
    url(r'^change_password/$', ChangePasswordView.as_view()),
    url(r'^update/$', UpdateUserView.as_view()),
    url(r'^del/$', DeleteUserView.as_view()),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view()),
]