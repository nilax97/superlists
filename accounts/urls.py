from django.urls import re_path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    re_path(r'^send_login_email$', views.send_login_email, name='send_login_email'),
    re_path(r'^login$', views.login, name='login'),
    re_path(r'^logout$', LogoutView.as_view(next_page='/'), name='logout'),
]