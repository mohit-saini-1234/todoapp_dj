from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path as url
from django.contrib.auth import views as auth_views
from user.views import UserReg ,UserGet,UserPost
# # urlpatterns = [
# #     url(r'^login/$', UserAuth.as_view()),
# #     url(r'^profile/$', UserProfile.as_view()),
# #     url(r'^register/$', UserRegister.as_view()),
# #     url(r'^change_password/$', ChangePasswordView.as_view()),
# #     url(r'^update/$', UpdateUserView.as_view()),
# #     url(r'^del/$', DeleteUserView.as_view()),
# #     path('password_change_done/', auth_views.PasswordChangeDoneView.as_view()),
# # ]
urlpatterns = [
    url(r'^reg/$', UserReg.as_view()),
    url(r'^pro/$', UserGet.as_view()),
    url(r'^log/$', UserPost.as_view()),]
