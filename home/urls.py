from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', view=views.get_home, name='home'),
    path('contact/', view=views.get_contact, name='contact'),
    path('register/', view=views.register, name='register')
]
