from django.urls import path
from . import views

urlpatterns = [
    path('jurisprudencia/', views.busca_documentos, name='jurisprudencia'),
]
