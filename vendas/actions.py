from django.http import HttpResponseNotFound

'''
https://docs.djangoproject.com/en/4.2/ref/contrib/admin/actions/
Registrando actions no admin
No exemplo abaixo registramos duas actions
que setam um booleano como False ou True
Nesse caso o field nfe_emitida

'''
def nfe_emitida(modeladmin, request, queryset):
    '''
    Define nota fiscal emitida True se usuário tiver permissão
    Abaixo uma permissão personalizada setar_nfe
    criada em Meta models Vendas
    Mesmo que seja supaer_user nãso consegue se não tiver esta permissão
    '''
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)
    else:
        return HttpResponseNotFound('<h1>Sem permissao</h1>')


'''
Descrição da action
'''
nfe_emitida.short_description = "NF-e emitida"


def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)

nfe_nao_emitida.short_description = "NF-e nao emitida"
