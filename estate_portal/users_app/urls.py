from django.urls import path
from django.contrib.auth import views as auth_views
from users_app.views import signup_view

app_name = 'users_app'

urlpatterns = [
    path("signup/", signup_view, name='signup'),

    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="users_app:login"),
        name="logout"
    )
]