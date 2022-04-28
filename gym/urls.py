from django.urls import path

from .views import (ConsultorFormView, ConsultoriaTemplateView,
                    IndexTemplateView, SuplementacaoTemplateView,
                    TreinosTemplateView)

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('consultoria', ConsultoriaTemplateView .as_view(), name='consultoria'),
    path('suplementacao', SuplementacaoTemplateView .as_view(), name='suplementacao'),
    path('treinos', TreinosTemplateView .as_view(), name='treinos'),
    path('formulario/<int:pk>/',
         ConsultorFormView.as_view(), name='formulario'),
]
