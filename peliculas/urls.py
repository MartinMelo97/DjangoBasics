from django.urls import path
from .views import PeliculasListView, PeliculasDetailView, PeliculasCreateView, PeliculasEditView, PeliculasDeleteView
app_name = "peliculas"

urlpatterns = [
    path('', PeliculasListView.as_view(), name="movie_list"),
    path('<int:pelicula_id>', PeliculasDetailView.as_view(), name="movie_detail"),
    path('create', PeliculasCreateView.as_view(), name="movie_create"),
    path('edit/<int:pelicula_id>', PeliculasEditView.as_view(), name="movie_edit"),
    path('delete/<int:pelicula_id>', PeliculasDeleteView.as_view(), name="movie_delete")
]