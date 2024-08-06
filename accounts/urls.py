from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pacientes/<str:pk_test>', views.pacientes, name='pacientes'),
    path('medicos/<str:pk_test>/', views.medicos, name='medicos'),
    
    path('adicionar_consulta/<int:medico_id>/', views.adicionar_consulta, name='adicionar_consulta'),
    path('atualizar_consulta/<int:medico_id>/<int:id>/', views.atualizar_consulta, name='atualizar_consulta'),
    
    path('processar_input/', views.processar_input, name='processar_input'),
]
