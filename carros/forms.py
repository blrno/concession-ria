import re
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrarForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_password1(self):
        password = self.cleaned_data.get("password1")

        if password:
            if len(password) < 8:
                raise forms.ValidationError(
                    "A senha deve ter no mínimo 8 caracteres."
                )
            if not re.search(r'[0-9]', password):
                raise forms.ValidationError(
                    "A senha precisa de pelo menos um número."
                )
            if not re.search(r'[A-Z]', password):
                raise forms.ValidationError(
                    "A senha precisa de pelo menos uma letra maiúscula."
                )
            if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
                raise forms.ValidationError(
                    "A senha precisa de um caractere especial (@, #, $...)."
                )

        return password
    
    # No final do seu arquivo forms.py
from .models import Carro # Importe o modelo Carro que você criou

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['nome', 'marca', 'ano', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }