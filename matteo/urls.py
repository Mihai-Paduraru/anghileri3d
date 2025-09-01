from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    # Aggiungi queste URL per le pagine dei progetti statici

    path('portfolio/ue-cinematic/', 
         TemplateView.as_view(template_name='matteo/ue_cinematic.html'), 
         name='ue_cinematic'),

    path('portfolio/the-golden-fall/', 
         TemplateView.as_view(template_name='matteo/the_golden_fall.html'), 
         name='the_golden_fall'),
    
    path('portfolio/rise-of-the-badlands-vehicle/', 
         TemplateView.as_view(template_name='matteo/rise_of_the_badlands_vehicle.html'), 
         name='rise_of_the_badlands_vehicle'),
    
    path('portfolio/cafe/', 
         TemplateView.as_view(template_name='matteo/cafe.html'), 
         name='cafe'),
    
    path('portfolio/bar/', 
         TemplateView.as_view(template_name='matteo/bar.html'), 
         name='bar'),
    
    path('portfolio/zbrush-project/', 
         TemplateView.as_view(template_name='matteo/zbrush_project.html'), 
         name='zbrush_project'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)