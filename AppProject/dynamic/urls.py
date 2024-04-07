"""
将视图函数添加到urlpatterns列表中，并为每个URL配置指定了相应的路径和视图函数。这样可以将不同的请求映射到对应的视图函数上，实现各种功能的API
！！！！！在Django项目的settings.py文件中找到INSTALLED_APPS设置，确保auth_app应用程序已添加到INSTALLED_APPS列表中！！！！
"""
from django.urls import path
from . import views

urlpatterns = [
    path('publish_content/', views.publish_content, name='publish_content'),
    path('edit_content/<int:content_id>/', views.edit_content, name='edit_content'),
    path('delete_content/<int:content_id>/', views.delete_content, name='delete_content'),
    path('list_content/', views.list_content, name='list_content'),
    path('content_detail/<int:content_id>/', views.get_content_detail, name='get_content_detail'),
    path('publish_comment/<int:post_id>/', views.publish_comment, name='publish_comment'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('unlike_comment/<int:comment_id>/', views.unlike_comment, name='unlike_comment'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('unlike_post/<int:post_id>/', views.unlike_post, name='unlike_post'),

    # path('follow_user/<int:user_id>/', views.follow_user, name='follow_user'),
    # path('unfollow_user/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
    # path('search/', views.search, name='search'),
    # path('recommend/<int:user_id>/', views.recommend, name='recommend'),
]