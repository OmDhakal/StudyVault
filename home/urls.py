from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("resources", views.resourses, name="resources"),
    path("library", views.library, name="library"),
    path("login", views.user_login, name="login"),
    path("register", views.user_register, name="register"),
    path("profile", views.profile, name="profile"),
    path("logout", views.user_logout, name="logout"),
]
