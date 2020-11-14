from django.shortcuts import render
from django.http import HttpResponseRedirect ,HttpResponse
from django.views.generic import (
    TemplateView, ListView, DetailView, FormView
)
# from .models import 


class Home(TemplateView):
    # model = Recipe
    template_name = 'index.html'


class Contact(TemplateView):
    # model = 
    # context_object_name = "contact"
    template_name = 'contact.html'


class Recipes(TemplateView):
    # model = 
    # context_object_name = "recipe"
    template_name = 'recipes.html'



class Stories(TemplateView):
    # model = 
    # context_object_name = "stories"
    template_name = 'strories.html'

class About(TemplateView):
    # model = 
    # context_object_name = "about"
    template_name = 'about.html'
