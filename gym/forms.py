

from django import forms


class ConsultorForm(forms.Form):
    nome = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    email2 = forms.EmailField(
        max_length=255)
    cartao = forms.CharField(
        max_length=255)
    numero = forms.CharField(
        max_length=255)
