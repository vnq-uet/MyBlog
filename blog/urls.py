from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.show_list_post, name='show_list_post'),
    path('<int:pk>/', view=views.show_detail_post, name='show_detail_post'), 
    path('<int:post_id>/like/', view=views.like, name='post_like'),
    
]
