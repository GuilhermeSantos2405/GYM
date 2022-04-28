from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from .forms import ConsultorForm
from .models import Consultor, Home, Suplementacao, Treinos


class ConsultoriaTemplateView(ListView):
    template_name = 'consultoria.html'
    model = Consultor


class ConsultorFormView(FormView, DetailView):
    template_name = 'formulario.html'
    form_class = ConsultorForm
    model = Consultor
    context_object_name = 'consultor'


class IndexTemplateView(ListView):
    template_name = 'index.html'
    model = Home


class TreinosTemplateView(ListView):
    template_name = 'treinos.html'
    model = Treinos


class SuplementacaoTemplateView(ListView):
    template_name = 'suplementacao.html'
    model = Suplementacao
