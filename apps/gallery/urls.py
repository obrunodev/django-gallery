from apps.gallery import views

from django.urls import path

app_name = 'gallery'
urlpatterns = [
    path('', views.gallery_index, name='index'),
]
