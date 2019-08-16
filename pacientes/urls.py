from django.urls import path
from . import  views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('dashboard/',views.dashboardView,name='dashboard'),
    path('',LoginView.as_view(),name='login_url'),
    path('logout/',LogoutView.as_view(next_page='login_url'),name='logout'),
    path('new/', views.paciente_new, name='paciente_new'),
    path('estadistica/', views.estadistica, name='estadistica'),
]