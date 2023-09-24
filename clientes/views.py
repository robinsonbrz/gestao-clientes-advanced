from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from produtos.models import Produto
from vendas.models import Venda
from .forms import PersonForm
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy


@login_required
def persons_list(request):
    # Possível implementar um filtro aqui
    # Recebendo de um request.GET.get()
    # mas precisamos criar um form no front
    persons = Person.objects.all()

    return render(
        request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    # verificando tipo de permissão do usuário logado
    # app clientes permissão de add modleo Person
    # checando manualmente
    if not request.user.has_perm('clientes.add_person'):
        return HttpResponse('Nao autorizado')
    elif not request.user.is_superuser:
        return HttpResponse('Nao e superusuario')

    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


class PersonList(LoginRequiredMixin, ListView):
    '''
    Classe herda de List view e de LoginRequiredMixin   


    '''
    model = Person

    # sobrescrevendo o método get_context_data  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ler a sessão a variável primeiro acesso
        # se não existir passa false
        primeiro_acesso = self.request.session.get('primeiro_acesso', False)

        # caso não tenha sido acessado salva mensagem na sessão
        if not primeiro_acesso:
            context['message'] = 'Seja bem vindo ao seu primeiro acesso hoje'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'Voce ja acessou hoje'

        return context

class PersonDetail(LoginRequiredMixin, DetailView):
    '''
    CBV DetailView
    Utilizada para receber detalhes de um modelo
    '''
    model = Person
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        # sobrescrevendo o método com select_related aumentando a performance
        return Person.objects.select_related('doc').get(id=pk)
    
    # sobrescrevendo o método get_context_data  de contextmixin
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Venda.objects.filter(
            pessoa_id=self.object.id)
        return context


class PersonCreate(LoginRequiredMixin, CreateView):
    '''
    CBV relates to a form injects a form with these fields on template
    '''
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'


class PersonUpdate(LoginRequiredMixin, UpdateView):
    '''
    CBV UpdateView relates to a form injects a form with these fields on template
    used for update an specific item 
    receives an id on urls
    path('person_update/<int:pk>/', PersonUpdate.as_view(), name='person_update_cbv'),
    Besides that it loads the form with the model data for this specific id

    '''
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')


class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''
    CBV UpdateView 
    used for update an specific item 
    receives an id on urls
    path('person_delete/<int:pk>/', PersonDelete.as_view(), name='person_delete_cbv'),
    Needs a form with a delete button to delete his specific id

    '''
    # descrevendo o tipo de permissão necessária para PermissionRequiredMixin
    permission_required = ('clientes.deletar_clientes',)

    model = Person
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        '''
        Esse método pode ser utilizado na maioria das CBV e é executado no sucesso 
        da CBV
        to determine the URL where the user should be redirected after a successful action, 
        such as submitting a form or saving an object.
        This method helps manage the flow of the user interface and provides a
        seamless experience for users interacting with your web application.
        '''
        return reverse_lazy('person_list_cbv')


class ProdutoBulk(View):
    def get(self, request):
        # tudo se inicia com uma lista de dados de qualquer procedência. Excel...
        produtos = ['Banana', 'Maca', 'Limao', 'Laranja', 'Pera', 'Melancia']
        # iniciamos uma lista que será enviada ao banco em uma só operação
        list_produtos = []

        for produto in produtos:
            # criamos pbjetos do tipop produto
            p = Produto(descricao=produto, preco=10)
            # acrescentamos os objetos um a um em uma lista
            list_produtos.append(p)

        # Enviamos todos os objetos para o banco de uma vez
        # Nesse caso em apenas uma query com todos os dados para o banco
        # O oposto disso seria objects.save() que salva um único objeto
        # ou seja cria uma query para cada save
        Produto.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')


def api(request):
    """
    Returns a JSON response containing a list of dictionaries representing 'Produto' objects from the database.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: A JSON response with a list of dictionaries representing 'Produto' objects.
    :rtype: JsonResponse
    """

    a = {'nome': 'Gregory', 'idade': 29, 'salario': 500}
    mensagem = {'mensagem': 'erro xyz'}
    lista = [1, 2, 3]

    produto = Produto.objects.last()

    b = model_to_dict(produto)

    l = []

    produtos = Produto.objects.all()

    for produto in produtos:
        l.append(model_to_dict(produto))

    return JsonResponse(l, status=200, safe=False)


class APICBV(View):
    def get(self, request):
        data = {'nome': 'Gregory'}

        produto = Produto.objects.last()
        b = model_to_dict(produto)

        l = []
        produtos = Produto.objects.all()

        for produto in produtos:
            l.append(model_to_dict(produto))

        return JsonResponse(l, safe=False)

    def post(self):
        pass
