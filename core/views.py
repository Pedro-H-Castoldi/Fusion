from django.views.generic import FormView # FormView pq temos um formulário em nossa página (index).
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Servico, Funcionario, Features
from .forms import ContaroForm

class IndexView(FormView):
    template_name = 'index.html' # Indica o nome do nosso template.
    form_class = ContaroForm # Indica o nome da nossa classe.
    success_url = reverse_lazy('index') # Indica para onde iremos levar os dados do nosso formulário.

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['features1'] = Features.objects.all()[:3]
        context['features2'] = Features.objects.all()[3:6]
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'E-mail enviado com sucesso.')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar E-mail.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)