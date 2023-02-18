from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('adminuser', RedirectView.as_view(url=reverse_lazy('admin:index')), name='adminuser'),
 
    path('oxygen_emission/', views.oxygen_emission, name='oxygen_emission'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('homeappliances/', views.homeappliances, name='homeappliances'),
    path('waste/', views.waste, name='waste'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]