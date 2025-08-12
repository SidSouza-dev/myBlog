from django.urls import path
from .views import home_view, criar_post_view, sobre_view,post_detail_view,post_delete_view

urlpatterns = [
    path('',home_view,name='home'),
    path('criar-post/',criar_post_view,name='criar_post'),
    path('sobre/',sobre_view,name='sobre'),

    path('post/<int:post_id>/', post_detail_view, name='post_detail'),
    path('post/<int:post_id>/delete',post_delete_view,name='post_delete')
]