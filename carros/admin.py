from django.contrib import admin
from .models import Carro

class CarroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'ano', 'preco_formatado', 'vendido')
    search_fields = ('nome', 'marca')
    list_filter = ('marca', 'vendido')

    def preco_formatado(self, obj):
        return f"R$ {obj.preco}"
        preco_formatado.short_description = 'Preço'

admin.site.register(Carro, CarroAdmin)