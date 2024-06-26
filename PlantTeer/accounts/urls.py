from django.urls import path
from . import views

app_name  = "accounts"

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("/profile/<username>/", views.profile, name="profile"),
    path("/profile/<username>/update/", views.update_profile, name="update_profile"),
     
]