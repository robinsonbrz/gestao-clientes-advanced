from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View


def calcular(v1, v2):
    return v1 / v2


def home(request):
    #    import pdb; pdb.set_trace()
    value1 = 10
    value2 = 20
    res = calcular(value1, value2)
    return render(request, 'home/home.html', {'result': res})


def my_logout(request):
    logout(request)
    1 + 1
    return redirect('home')


class HomePageView(TemplateView):
    '''
    Tipo class based view herda de TemplateView
    '''
    template_name = 'home2.html'

    def get_context_data(self, **kwargs):
        # super invoca get_context_data de super que é TemplateView
        # Template view por sua vez em sua definição possui ContextMixin em sua definição
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Ola, seja bem vindo ao curso de Django advanced.Frase recebida por contexto'
        return context


class MyView(View):
    '''
    Tipo class based view mais genérica póssivel herda de View
    '''
    def get(self, request, *args, **kwargs):
        response = render_to_response('home3.html')
        # Setando um cookie com um valor que será enviado na respose
        response.set_cookie('color', 'blue', max_age=1000)
        
        # lendo um cookie da sessão pelo nome 
        # nome color
        mycookie = request.COOKIES.get('color')
        print(mycookie)
        return response

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')
# FBV
# CBV
