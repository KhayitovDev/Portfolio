from django.urls import path
from .views import HomePageListView, AboutPageView, ProjectListView, ProjectDetailView
urlpatterns = [
    path('', HomePageListView.as_view(), name='home_page'),
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('projects/', ProjectListView.as_view(), name='projects_page'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail')
]
