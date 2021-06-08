 
from django.urls import path, include
from . import views

urlpatterns = [
    path('members/<str:team>/',views.get_members,name='team-members'),
    path('member/<int:pk>/',views.get_member,name='get-member'),
    path('add-member/',views.add_member,name='add-member'),
    path('update-member/<int:pk>/',views.update_member,name='update-member'),
    path('delete-member/<int:pk>/',views.delete_member,name='delete-member'),
    path('blog/new/', views.new_blog, name='new-blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('blog/<int:pk>/update', views.blog_update, name='blog-update'),
    path('blog/<int:pk>/delete', views.blog_delete, name='blog-delete'),
]
