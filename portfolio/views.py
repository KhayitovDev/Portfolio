from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import AboutModel, ProjectModel
# Create your views here.

class HomePageListView(TemplateView):
    template_name='index.html'

class AboutPageView(ListView):
    template_name='about.html'
    queryset=AboutModel.objects.all()
    context_object_name='details'

class ProjectListView(ListView):
    template_name='project-list.html'
    queryset=ProjectModel.objects.all()
    context_object_name='projects'

class ProjectDetailView(DetailView):
    template_name='project-detail.html'
    queryset=ProjectModel.objects.all()
    context_object_name='project_detail'