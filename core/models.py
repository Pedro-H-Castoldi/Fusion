import uuid
from django.db import models
from stdimage.models import StdImageField

# A biblioteca uuid serve para impedir conflitos de nomes, iremos usar-la para inpedir q haja conflito entre nome de imagens.
def get_file_name(_instance, filename):
    ext = filename.split('.')[-1] # Pega o ultimo caracter separado pelo split, ou seja, o ultimo nome depois do '.' (EX: png).
    filename = f'{uuid.uuid4}.{ext}'
    return filename

class Base(models.Model):
    criacao = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('modificado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICE = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    servico = models.CharField('Servico', max_length=30)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', choices=ICONE_CHOICE, max_length=12)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Funcionario(Base):

    nome = models.CharField('nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_name, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Fazebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome

class Features(Base):
    ICONE_CHOICE = (
        ('lni-laptop-phone', 'Notebook'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Design'),
    )

    recurso = models.CharField('Recurso', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone', choices=ICONE_CHOICE, max_length=16)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.recurso