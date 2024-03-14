from django.urls import path
from . import views

app_name = 'voting'
urlpatterns = [
    path('', views.index, name='index'),
    path('upvote/<int:target_id>/', views.upvote, name='upvote'),
    path('downvote/<int:target_id>/', views.downvote, name='downvote'),
    path('add_target/', views.add_target, name='add_target'),
    path('add_group/', views.add_group, name='add_group'),   
    path('group_targets/<str:group_name>/', views.group_targets, name='group_targets'),   
    
]
