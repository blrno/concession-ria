from django.urls import path
from django.contrib.auth import views as auth_views # Importe isso!
from . import views

urlpatterns = [
    # Usa a view pronta do Django, apontando para o seu arquivo html
    path('', auth_views.LoginView.as_view(template_name='carros/login.html'), name='login'),
    
    path('estoque/', views.lista_carros, name='lista_carros'),
    path('novo/', views.cadastrar_carro, name='cadastrar_carro'),
    path('excluir/<int:id>/', views.excluir_carro, name='excluir_carro'),
    
    # Logout pronto do Django
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]