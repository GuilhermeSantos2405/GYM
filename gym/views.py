from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class DietaTemplateView(TemplateView):
    template_name = 'dieta.html'


class ConsultoriaTemplateView(TemplateView):
    template_name = 'consultoria.html'


class TreinosTemplateView(TemplateView):
    template_name = 'treinos.html'


class SuplementacaoTemplateView(TemplateView):
    template_name = 'suplementacao.html'
