# from rest_framework.routers import DefaultRouter
# from . import views

# router = DefaultRouter()
# router.register(r'',  views.FormAFMListCreateView, basename='formAFM')
# urlpatterns = router.urls

from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import  FormAFMListCreateView, FormAFMRetrieveUpdateDestroyView

urlpatterns = [
    path('', FormAFMListCreateView.as_view(), name='formulario/AFM/'),
    # path('formAFM/<int:pk>/', FormAFMRetrieveUpdateDestroyView.as_view(), name='formulario/AFM/<int:pk>/'),
]