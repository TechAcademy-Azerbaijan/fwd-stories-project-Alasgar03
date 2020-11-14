from django.urls import path

from . import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('recipes/', views.Recipes.as_view(), name='recipes'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('stories/', views.Stories.as_view(), name='stories'),
    
    ]
