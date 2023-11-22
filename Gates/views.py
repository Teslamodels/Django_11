from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Bill(TemplateView):
    template_name = 'index.html'

class Gates(TemplateView):
    template_name = 'gates.html'
