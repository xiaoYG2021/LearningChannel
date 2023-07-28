from django.urls import path

from . import views

app_name = 'religion'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('logout', views.logout_view, name='logout',)
]
