from django.urls import re_path
from accounts import views

urlpatterns = [
    re_path(r'^send_email$', views.send_login_email, name='send_login_email'),
]