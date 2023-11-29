from django.urls import path
from . views import UserRegisterView,UserEditView,PasswordsChangeView,ShowProfileView,EditProfileView,CreateProfileView
from  django.contrib.auth import views as auth_views
from . import views
urlpatterns =[
    # path('home/',views.home,name="home")
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/', UserEditView.as_view(), name='profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('passwordsu/',PasswordsChangeView.as_view(template_name='registration/change-password.html'),name="password"),
    path('password_success/', views.password_success,name='password_success'),
    path('user_profile/<int:pk>', ShowProfileView.as_view(), name="user_profile"),
    path('Edit_profile/<int:pk>', EditProfileView.as_view(), name="Edit_profile"),
    path('Create_profile/', CreateProfileView.as_view(), name="create_profile"),

]