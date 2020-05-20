from django.views.generic import FormView # FormView pq temos um formulário em nossa página (index).
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils import translation

from .models import Servico, Funcionario, Features
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html' # Indica o nome do nosso template.
    form_class = ContatoForm # Indica o nome da nossa classe.
    success_url = reverse_lazy('index') # Indica para onde iremos levar os dados do nosso formulário.

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['features1'] = Features.objects.all()[:3]
        context['features2'] = Features.objects.all()[3:6]
        context['lang'] = lang
        translation.activate(lang)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, _('E-mail enviado com sucesso.'))
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar E-mail.'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)