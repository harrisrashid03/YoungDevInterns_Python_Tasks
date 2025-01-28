from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    path('publications/', views.publications, name='publications'),
    path('certifications/', views.certifications, name='certifications'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
]
