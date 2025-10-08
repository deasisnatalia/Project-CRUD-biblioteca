from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'anio', 'categoria', 'disponible']
    list_filter = ['categoria', 'disponible']
    search_fields = ['titulo', 'autor']