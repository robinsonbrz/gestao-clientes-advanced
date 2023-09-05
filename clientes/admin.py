from django.contrib import admin
from .models import Person, Documento


class PersonAdmin(admin.ModelAdmin):
    # fields= seriam campos do model que desejamos que seja exibido no admin do django
    # podemos exibir todos e utilizar o 
    # exclude = para excluir algum campo do model
    # podemos utilizar o fieldsets para organizar os campos do model
    

    fieldsets = (
        ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc', 'telefone')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary', 'photo')
        })
    )
    # fields = (('doc', 'first_name'), 'last_name', ('age', 'salary'), 'bio', 'photo')
    # exclude = ('bio', )
    list_filter = ('age', 'salary')
    # Set list_display to control which fields are displayed on the change list page of the admin
    list_display = ('doc', 'first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto')
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
