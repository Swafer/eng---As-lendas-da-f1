from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class indexview(View):
    def get(self, request):
        return render(request, 'index.html',)
    def post(self, request):
        pass

class LendasF1View(View):
    def get(self, request):
        carros = Carro.objects.all()
        circuitos = Circuito.objects.all()
        temporadas = Temporada.objects.all()
        equipes = Equipe.objects.all()

        context = {
            'carros': carros,
            'circuitos': circuitos,
            'temporadas': temporadas,
            'equipes': equipes,
        }

        return render(request, 'carros.html', context)

    
class LendasF2View(View):
    def get(self, request):
        carros = Carro.objects.all()
        circuitos = Circuito.objects.all()
        temporadas = Temporada.objects.all()
        equipes = Equipe.objects.all()

        context = {
            'carros': carros,
            'circuitos': circuitos,
            'temporadas': temporadas,
            'equipes': equipes,
        }

        return render(request, 'tabelas2.html', context)