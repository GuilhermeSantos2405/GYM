from django.urls import path

from .views import (ConsultoriaTemplateView, DietaTemplateView,
                    IndexTemplateView, SuplementacaoTemplateView,
                    TreinosTemplateView)

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('dieta', DietaTemplateView.as_view(), name='dieta'),
    path('consultoria', ConsultoriaTemplateView .as_view(), name='consultoria'),
    path('suplementacao', SuplementacaoTemplateView .as_view(), name='suplementacao'),
    path('treinos', TreinosTemplateView .as_view(), name='treinos'),
]
