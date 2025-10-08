from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro

class LibroListView(ListView):
    model = Libro
    template_name = 'libros/libro_list.html'
    context_object_name = 'libros'
    paginate_by = 5

class LibroCreateView(CreateView):
    model = Libro
    fields = ['titulo', 'autor', 'anio', 'disponible', 'categoria', 'imagen']
    template_name = 'libros/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroUpdateView(UpdateView):
    model = Libro
    fields = ['titulo', 'autor', 'anio', 'disponible', 'categoria', 'imagen']
    template_name = 'libros/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'libros/libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')