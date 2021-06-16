from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('hero_hero/', views.hero_hero, name='hero_hero'),
    path('hero_class/', views.hero_class, name='hero_class'),
    path('equipment/', views.equipment, name='equipment'),
    # path('register/', views.register, name='register'),

   
    

]
