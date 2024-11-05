# gestor/urls.py
from django.urls import path
from . import views
from .views import CaseListView, CaseDetailView, logout_view, upload_document
from django.views.generic import TemplateView 

urlpatterns = [
    path('', views.home_redirect, name='home_redirect'),
    path('cases/', CaseListView.as_view(),
         name='case-list'),  # URL para la lista de casos
    path('cases/<int:pk>/', CaseDetailView.as_view(),
         name='case-detail'),  # URL para el detalle de cada caso
     path('logout/', logout_view, name='logout'),
     path('upload/', upload_document, name='upload-document'),

]
