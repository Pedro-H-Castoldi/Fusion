from django.test import TestCase
from core.forms import ContatoForm

class ContatoFromTestCase(TestCase):

    def setUp(self):
        self.nome = 'Junihno'
        self.email = 'juninho.parrudao@gogmail.com'
        self.assunto = 'Tô latindo demais!'
        self.mensagem = 'Estou atacadão, latindo muito.'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados) # ContatoForm(request.POST) # É isso q ocorre por debaixo dos panos.

    def test_send_email(self):
        # Criar formulário 1 pegando os dados do self.dados
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_email()

        # Criar formulário 2 com os dados do self.form
        form2 = self.form
        form2.is_valid()
        res2 = form2.send_email()

        # Ver se res1 é igual à res2
        self.assertEquals(res1, res2)