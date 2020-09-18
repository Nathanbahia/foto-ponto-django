from django.urls import path
from .views import index, historico, visualizar_foto


urlpatterns = [
    path('', index, name='index'),
    path('historico', historico, name='historico'),
    path('visualizacao/<int:pk>', visualizar_foto, name='visualizar')
]