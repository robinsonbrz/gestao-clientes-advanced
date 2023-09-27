from django.contrib import admin
from .models import Person, Documento


class PersonAdmin(admin.ModelAdmin):
    # podemos utilizar o fieldsets para organizar os campos do model
    # agrupados e com opção de colapse
    fieldsets = (
        # agrupamentos de dados pessoais
        ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc', 'telefone')}),
        # agrupamentos de dados complemetares
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary', 'photo')
        })
    )

    # fields= seriam campos do model que desejamos que seja exibido no admin do django
    # podemos exibir todos e utilizar o 
    # exclude = para excluir algum campo do model
    # abaixo um exemplo do uso de fields
    # cada tupla será uma linha no formulário admin como mostrado abaixo
    # ('doc', 'first_name'), 
    #'last_name', 
    #('age', 'salary'), 
    # 'bio', 'photo'
    # fields = (('doc', 'first_name'), 'last_name', ('age', 'salary'), 'bio', 'photo')
    # exclude = ('bio', )

    # Set list_filter to activate filters in the right sidebar of the change list page of the admin.
    list_filter = ('age', 'salary')
    # Set list_display to control which fields are displayed on the change list page of the admin
    list_display = ('doc', 'first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto')
    #Set search_fields to enable a search box on the admin change list page. 
    # This should be set to a list of field names that will be searched 
    # whenever somebody submits a search query in that text box.
    search_fields = ('id', 'first_name')
    autocomplete_fields = ['doc']


    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Nao'

    tem_foto.short_description = 'Possui foto'


class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc']


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)
