from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("Login/", LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path("", indexview.as_view(), name="index"),  # Rota para a página inicial
    path('carros/', LendasF1View.as_view(), name='carros'),  # Rota para a página de 
    path('tabelas2/', LendasF2View.as_view(), name='tabelas2'),  # Rota para a página de tabelas2
    path('logout/', LogoutView.as_view(), name='logout'),
]