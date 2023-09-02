from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    '''
    Template tag personalizado
    Retorna a data e hora atual
    exemplo de uso :
    no template.html
    {% carregar com load mytags %}
             {{ current_time:"%d/%m/%Y %H:%M:%S" }}
    '''
    return datetime.now().strftime(format_string)


@register.simple_tag
def footer_message():
    return 'Desenvolvimento web com Django 2.0.2'

