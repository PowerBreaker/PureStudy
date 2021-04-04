from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('read', views.read, name='read'),
    path('chapter/<chapter_id>', views.get_chapter, name='chapter'),
    path('course/<course_id>', views.get_course, name='course'),
]