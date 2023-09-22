from django import forms


class ItemPedidoForm(forms.Form):
    produto_id = forms.CharField(label='ID do Produto', max_length=100)
    quantidade = forms.IntegerField(label='Quantidade')
    desconto = forms.DecimalField(label='Desconto', max_digits=7, decimal_places=2)



class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino')])

'''
# Exemplo de uso:

form = MyForm()

# Preenche o form com dados do usuário:

form.cleaned_data['name'] = 'João da Silva'
form.cleaned_data['gender'] = 'M'

# Valida o form:

if form.is_valid():
    print(form.cleaned_data)

Utilize o código para gerar o seguinte formulário HTML:

HTML
<form action="/" method="post">
    <input type="text" name="name" placeholder="Nome">
    <select name="gender">
        <option value="M">Masculino</option>
        <option value="F">Feminino</option>
    </select>
    <input type="submit" value="Enviar">
</form>





'''