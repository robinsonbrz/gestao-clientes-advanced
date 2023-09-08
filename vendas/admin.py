from django.contrib import admin
from .models import Venda
from .models import ItemDoPedido
from .actions import nfe_emitida, nfe_nao_emitida


class ItemPedidoInline(admin.TabularInline):
    # TabularInLine é um tipo de inline que permite que os campos sejam exibidos em uma tabela
    # como itens de pedido e link para janela many to many dos produtos
    model = ItemDoPedido
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    '''
    O autocomplete_fields é um campo que faz com que o campo de busca seja automaticamente preenchido
    como um select2
    '''
    autocomplete_fields = ("pessoa",)
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id', 'numero', 'pessoa', 'nfe_emitida', 'valor')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]

    # Adicionando um inline para os itens de pedido
    inlines = [ItemPedidoInline]

    '''
    adicionando m2m com produtos em admin
    
    '''
    filter_vertical = ['produtos']


    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)
