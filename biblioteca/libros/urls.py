from django.urls import path
from .views import LibroListView, LibroCreateView, LibroUpdateView, LibroDeleteView

urlpatterns = [
    path('', LibroListView.as_view(), name='libro_list'),
    path('crear/', LibroCreateView.as_view(), name='libro_create'),
    path('<int:pk>/editar/', LibroUpdateView.as_view(), name='libro_update'),
    path('<int:pk>/eliminar/', LibroDeleteView.as_view(), name='libro_delete'),
]