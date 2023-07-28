from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('<slug:username>/', views.user_view, name='user'),
    path('edit-homepage', views.edit_homepage_view, name='edit-homepage'),
]
