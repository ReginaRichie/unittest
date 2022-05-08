"""Определяет схемы URL для пользователей"""


from django.conf.urls import url
from . import views
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('register/', views.register, name='register'),
]
