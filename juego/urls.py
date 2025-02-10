from django.urls import path
from .views import iniciar_juego, jugar

urlpatterns = [
    path('', iniciar_juego, name='iniciar_juego'),  # Página de inicio que genera el número
    path('jugar/', jugar, name='jugar'),  # Página donde se juega
]
