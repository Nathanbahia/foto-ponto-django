from django.urls import path
from .views import index, historico


urlpatterns = [
    path('', index, name='index'),
    path('historico', historico, name='historico')
]