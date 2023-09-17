from django.db import models
# envio de email django
from django.core.mail import send_mail, mail_admins, send_mass_mail
from django.template.loader import render_to_string


class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        permissions = (
            ('deletar_clientes', 'Deletar clientes'),
        )
        unique_together = (("first_name", "telefone"),)

    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)

        data = {'cliente': self.first_name}
        plain_text = render_to_string('clientes/emails/novo_cliente.txt', data)
        html_email = render_to_string('clientes/emails/novo_cliente.html', data)

        # envio de email a cada salvamento
        send_mail(
            'Novo cliente cadastrado',
            plain_text,
            'django@rob.com.br',
            ['django@rob.com.br'],
            html_message=html_email,
            fail_silently=False,
        )
        '''The fail_silently argument controls how the backend should 
        handle errors. If fail_silently is True, 
        exceptions during the email sending process will be silently ignored.
        '''

        mail_admins(
            'Novo cliente cadastrado',
            plain_text,
            html_message=html_email,
            fail_silently=False,
        )

        message1 = (
            'Subject here', 'Here is the message', 'django@gregorypacheco.com.br',
            ['django@gregorypacheco.com.br',])
        message2 = ('Another Subject', 'Here is another message', 'django@gregorypacheco.com.br',
                    ['django@gregorypacheco.com.br',])
        # send_mass_mail([message1, message2], fail_silently=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

'''
exemplo de conexão a uma tabela preexistente em um banco de dados
uma tabela que já existia antes da aplicação django
mas que precisamos conectar o Django a esta tabela
CREATE TABLE MinhaTabela2(
	id integer PRIMARY KEY,
	nome text NOT NULL,
	salario real NOT NULL
);


'''
class TabelaPreexistente(models.Model):
    nome = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        # ao Rodar o make migrations vai criar o migration dessa tabela que já esiste
        # Ao tentar rodar o migrate va dar um erro pq a tabela já existe
        # Vai tentar criar essa tabela
        # Para resolver isso basta rodar python manage.py migrate --fake

        # MinhaTabela2 é o nome da tabela que já existe no banco de dados
        db_table = 'MinhaTabela2'

    def __str__(self):
        return self.nome