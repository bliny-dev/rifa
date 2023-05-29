from django.urls import path
from . import views

urlpatterns = [
        path('gerir_sorteio/', views.gerir_sorteio, name="gerir_sorteio" ),
        path('gerir_sorteio/', views.adiciona_premio, name="adiciona_premio" ),

]
