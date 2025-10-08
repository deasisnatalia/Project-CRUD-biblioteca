from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias/categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categorias/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')