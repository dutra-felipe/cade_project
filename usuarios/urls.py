from django.urls import path
from . import views
from .views import EventosView, NotasView, NovidadesView, SobreView, CasosRecentesView

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('eventos/', EventosView.as_view(), name='eventos'),
    path('notas/', NotasView.as_view(), name='notas'),
    path('novidades/', NovidadesView.as_view(), name='novidades'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('casos/', CasosRecentesView.as_view(), name='casos'),
]
