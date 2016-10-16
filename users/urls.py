from django.conf.urls import url

from . import views

app_name = "user"

urlpatterns = [
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^signup/', views.user_signup, name="signup"),
    url(r'(?P<username>[\w\-]+)/', views.user_profile, name="profile"),
]