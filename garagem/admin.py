from django.contrib import admin

from garagem.models import Modelo, Marca, Cor, veiculo   

admin.site.register(Modelo)
admin.site.register(Marca)
admin.site.register(Cor)
admin.site.register(veiculo)

