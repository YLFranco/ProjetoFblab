from django.urls import path
from . import views 

urlpatterns = [
    path('criar_ar_condicionado', views.criar_ar_condicionado, name='criar_ar_condicionado'),
]
