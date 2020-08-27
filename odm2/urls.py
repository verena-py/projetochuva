from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.paginainicial, name='paginainicial'),
    path('projeto/', views.projeto, name='projeto'),
    path('consulta/', views.consulta, name='consulta'),
    path('dados/', views.dados, name='dados'),
    path('gantt/', views.gantt, name='gantt'),
    path('piacabucu/', views.piacabucu, name='piacabucu'),
    path('exportar/', views.exportar, name='exportar'),
    path('norte/', views.norte, name='norte')

]