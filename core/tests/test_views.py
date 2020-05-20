from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from core.views import IndexView

class IndexViewTestCase(TestCase):

    def setUp(self):
        # Criando um formulário
        self.dados = {
            'nome': 'Juninho',
            'email': 'juninhoparrudo@gogmail.com',
            'assunto': 'Latindo muito',
            'mensagem': 'Estou latindo descontroladamente.'
        }

        #Por meio desse método podemos criar requisição Post.
        self.Cliente = Client()

    def test_form_valid(self):
        # request recebe a indicação para onde os dados do formulário irá (reverse_lazy) e os dados dele (self.dados).
        request = self.Cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302) # O estatus de request tem q ser igual à 302, pois manda os dados do formulário para a mesma página.

    def test_form_invalid(self):
        dados_invalidos = {
            'nome': 'juninho',
            'email': 'juninhoparruco@dogmail.com'
        }

        # Note q os dados recebidos são os inválidos (incompleto).
        request = self.Cliente.post(reverse_lazy('index'), data=dados_invalidos)
        self.assertEquals(request.status_code, 200)