from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display= ['nome', 'categoria', 'preco', 'available', 'updated']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=['nome']
