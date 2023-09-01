from django import template

register = template.Library()

@register.filter
def arredonda(value, casas):
    '''
    Template tag personalizado
    Arredonda o valor para o número de casas informado
    exemplo de uso :
    numero a ser arredondado : 123.6548
    parâmetro numero de casas : 2
    resultado : 123.65
     
    {{ 123.6548| arredonda:2}}
    '''
    return round(value, casas)

