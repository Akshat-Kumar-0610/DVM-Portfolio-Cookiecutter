 
from django.urls import path, include
from . import views

urlpatterns = [
    path('members/<str:team>/',views.get_members,name='team-members'),
    path('member/<int:pk>/',views.get_member,name='get-member'),
    path('blog/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('project/<int:pk>/', views.get_project,name='get-project'),
    path('projects/', views.get_projects,name='get-projects-all'),
]
