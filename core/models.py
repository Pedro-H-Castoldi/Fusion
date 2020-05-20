import uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

# A biblioteca uuid serve para impedir conflitos de nomes, iremos usar-la para inpedir q haja conflito entre nome de imagens.
def get_file_name(_instance, filename):
    ext = filename.split('.')[-1] # Pega o ultimo caracter separado pelo split, ou seja, o ultimo nome depois do '.' (EX: png).
    filename = f'{uuid.uuid4}.{ext}'
    return filename

class Base(models.Model):
    criacao = models.DateField(_('Criação'), auto_now_add=True)
    modificado = models.DateField(_('modificado'), auto_now=True)
    ativo = models.BooleanField(_('Ativo?'), default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICE = (
        ('lni-cog', _('Engrenagem')),
        ('lni-stats-up', _('Gráfico')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
    )

    servico = models.CharField(_('Servico'), max_length=30)
    descricao = models.TextField(_('Descrição'), max_length=200)
    icone = models.CharField(_('Icone'), choices=ICONE_CHOICE, max_length=12)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField(_('Cargo'), max_length=100)

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')

    def __str__(self):
        return self.cargo

class Funcionario(Base):

    nome = models.CharField(_('nome'), max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name=_('Cargo'), on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    imagem = StdImageField(_('Imagem'), upload_to=get_file_name, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Fazebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')

    def __str__(self):
        return self.nome

class Features(Base):
    ICONE_CHOICE = (
        ('lni-laptop-phone', _('Notebook')),
        ('lni-cog', _('Engrenagem')),
        ('lni-leaf', _('Folha')),
        ('lni-layers', _('Design')),
    )

    recurso = models.CharField(_('Recurso'), max_length=100)
    descricao = models.TextField(_('Descricao'), max_length=200)
    icone = models.CharField(_('Icone'), choices=ICONE_CHOICE, max_length=16)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.recurso