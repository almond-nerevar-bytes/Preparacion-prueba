from django.contrib import admin
from .models import Categoria, Figura
# Register your models here.

admin.site.site_header = 'Panel de Administración del Catalogo de Figuras de UmaMusume'
admin.site.site_title = 'Mundo de Peluches/Figuras de UmaMusume'
admin.site.index_title = 'Panel de Administración del Catalogo de Figuras/Peluches de UmaMusume'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'activo', 'creado_en')
    search_fields = ('nombre', 'descripcion')
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ('activo',)

@admin.register(Figura)
class FiguraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'fabricante', 'precio_formateado', 'stock', 'activo', 'destacado')
    list_filter = ('categoria', 'fabricante', 'activo', 'destacado')
    search_fields = ('nombre', 'fabricante', 'descripcion')
    list_editable = ('stock', 'activo', 'destacado')
    prepopulated_fields = {'slug': ('nombre',)}
    list_per_page = 15