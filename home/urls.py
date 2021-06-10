from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', view=views.get_home, name='home'),
    path('contact/', view=views.get_contact, name='contact'),
    path('register/', view=views.register, name='register'),
    path('login/', view=auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', view=auth_views.LogoutView.as_view(next_page='/'), name='logout')
]
