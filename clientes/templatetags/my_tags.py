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

@register.filter
def soma(n1, n2):
    """
    Template tag personalizado
    Soma dois números
    exemplo de uso :
    numero 1 : 10
    numero 2 : 20
    resultado : 30
     
    {{ 10| soma:20}}
    """
    return n1 + n2
