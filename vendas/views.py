from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Venda
from .models import ItemDoPedido
from .forms import ItemPedidoForm


class DashboardView(View):
    """
    View class for displaying a sales dashboard.

    This view checks if the current user has the permission to view the dashboard.
    If the user has the 'vendas.ver_dashboard' permission, they are granted access.
    Otherwise, an 'Acesso negado' message is displayed.

    The dashboard displays various statistics related to sales orders, including the
    average, average with discounts, minimum, maximum, and counts of orders.

    Attributes:
        None

    Methods:
        - dispatch(self, request, *args, **kwargs): Checks user permissions and grants
          or denies access.
        - get(self, request): Retrieves and displays sales statistics on the dashboard.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response displaying the sales dashboard
        or an access denied message.
    """
    # sobrescrevendo o método dispatch que é o primeiro da class based view
    # para que ele faça a verificação de permissão do usuario
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso negado, voce precisa de permissao!')

        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = {}
        '''
        Foram criados managers em managers.py que chamam aggregates min, sum, avg
        para simplificar o código
        '''
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desconto()
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['n_ped'] = Venda.objects.num_pedidos()
        data['n_ped_nfe'] = Venda.objects.num_ped_nefe()

        return render(request, 'vendas/dashboard.html', data)


class NovoPedido(View):
    """
    View class for handling new sales order creation.

    GET: Renders the 'novo-pedido.html' template to display a new sales order form.

    POST: Processes the submitted form data, updates or creates a sales order,
    and renders the 'novo-pedido.html' template with the updated order details.

    Attributes:
        None

    Methods:
        - get(self, request): Renders the new sales order form.
        - post(self, request): Processes the form data, updates or creates a sales order,
        and renders the form with updated order details.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response containing the sales order form or order details.
    """
    # def get(self, request):
    #     return render(request, 'vendas/novo-pedido.html')

    # def post(self, request):
    #     data = {}
    #     data['form_item'] = ItemPedidoForm()
    #     data['numero'] = request.POST['numero']
    #     data['desconto'] = float(request.POST['desconto'].replace(',', '.'))
    #     data['venda_id'] = request.POST['venda_id']

    #     if data['venda_id']:
    #         venda = Venda.objects.get(id=data['venda_id'])
    #         venda.desconto = data['desconto']
    #         venda.numero = data['numero']
    #         venda.save()
    #     else:
    #         venda = Venda.objects.create(
    #             numero=data['numero'], desconto=data['desconto'])

    #     itens = venda.itemdopedido_set.all()
    #     data['venda'] = venda
    #     data['itens'] = itens
    #     return render(
    #         request, 'vendas/novo-pedido.html', data)


class NovoItemPedido(View):
    def get(self, request, pk):
        pass

    def post(self, request, venda):
        data = {}
        item = ItemDoPedido.objects.create(
            produto_id=request.POST['produto_id'], quantidade=request.POST['quantidade'],
            desconto=request.POST['desconto'], venda_id=venda)

        data['item'] = item
        data['form_item'] = ItemPedidoForm()
        data['numero'] = item.venda.numero
        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda
        data['itens'] = item.venda.itemdopedido_set.all()

        return render(
            request, 'vendas/novo-pedido.html', data)


class ListaVendas(View):
    def get(self, request):
        vendas = Venda.objects.all()
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas})


class EditPedido(View):
    def get(self, request, venda):
        data = {}
        venda = Venda.objects.get(id=venda)
        data['form_item'] = ItemPedidoForm()
        data['numero'] = venda.numero
        data['desconto'] = float(venda.desconto)
        data['venda'] = venda
        data['itens'] = venda.itemdopedido_set.all()

        return render(
            request, 'vendas/novo-pedido.html', data)


class DeletePedido(View):
    def get(self, request, venda):
        venda = Venda.objects.get(id=venda)
        return render(
            request, 'vendas/delete-pedido-confirm.html', {'venda': venda})

    def post(self, request, venda):
        venda = Venda.objects.get(id=venda)
        venda.delete()
        return redirect('lista-vendas')


class DeleteItemPedido(View):
    def get(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        return render(
            request, 'vendas/delete-itempedido-confirm.html', {'item_pedido': item_pedido})

    def post(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        venda_id = item_pedido.venda.id
        item_pedido.delete()
        return redirect('edit-pedido', venda=venda_id)
