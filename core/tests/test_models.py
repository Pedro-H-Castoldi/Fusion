import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_name

class GetFileNameTestCase(TestCase):
    def setUp(self):
        self.file = f'{uuid.uuid4()}.png'

    def test_get_file_name(self):
        teste = get_file_name(None, 'arquivo.png')
        self.assertTrue(len(self.file), len(teste))

class ServicoTestCase(TestCase):

    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):

    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):

    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)

class FeaturesTestCase(TestCase):

    def setUp(self):
        self.feature = mommy.make('Features')

    def test_str(self):
        self.assertEquals(str(self.feature), self.feature.recurso)
