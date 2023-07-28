from django.urls import path

from . import views

app_name = 'learning'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('search', views.search_view, name='search'),
    path('<slug:channel_title>/', views.channel_view, name='channel'),
    path('<slug:channel_title>/new', views.new_topic_view, name='new-topic'),
    path('<slug:channel_title>/delete/<int:topic_id>', views.delete_topic_view, name='delete-topic'),
    path('<slug:channel_title>/<int:topic_id>/', views.topic_view, name='topic'),
    path('<slug:channel_title>/<int:topic_id>/new', views.new_entry_view, name='new-entry'),
    path('<slug:channel_title>/<int:topic_id>/delete/<int:entry_id>', views.delete_entry_view, name='delete-entry'),
]
