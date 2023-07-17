from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('<int:course_id>', views.single_course, name='single_course'),
    path('register/', views.registration, name='registration'),
]
