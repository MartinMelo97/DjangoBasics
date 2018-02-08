from django.shortcuts import render, redirect
from django import views
from .models import Pelicula
from .forms import PeliculaForm

class PeliculasListView(views.View):

    def get(self, request):

        template_name="peliculas/list.html"
        peliculas = Pelicula.objects.all()
        context = {
            'peliculas':peliculas
        }

        return render(request, template_name, context)


class PeliculasDetailView(views.View):
    def get(self, request, pelicula_id):
        template_name="peliculas/detail.html"
        pelicula = Pelicula.objects.get(id=pelicula_id)
        context = {
            'pelicula':pelicula
        }
        return render(request, template_name, context)


class PeliculasCreateView(views.View):
    def get(self, request):
        template_name="peliculas/create.html"
        form = PeliculaForm()
        action = "create"
        context = {
            'form':form,
            'action':action
        }

        return render(request, template_name, context)

    def post(self, request):
        template_name="peliculas/create.html"
        form = PeliculaForm(request.POST, request.FILES)

        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.save()
            form.save_m2m()
            return redirect('peliculas:movie_list')
        else:
            error = "Hubo un error"
            action = "create"
            context = {'form':form, 'error':error,'action':action}
            return render(request, template_name, context)


class PeliculasEditView(views.View):
    def get(self, request, pelicula_id):
        template_name = "peliculas/create.html"
        pelicula = Pelicula.objects.get(id=pelicula_id)
        form = PeliculaForm(instance=pelicula)
        action="edit"
        context = {
            'form':form,
            'action':action,
            'id':pelicula_id
        }
        return render(request, template_name, context)

    def post(self,request,pelicula_id):
        pelicula = Pelicula.objects.get(id=pelicula_id)
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)

        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.save()
            form.save_m2m()
            return redirect('peliculas:movie_detail', pelicula_id)
        else:
            template_name = "peliculas/create.html"
            error = "No se pudo actualizar"
            action = "edit"
            context = {'form':form, 'error':error,'action':action,'id':pelicula_id}
            return render(request, template_name, context)

class PeliculasDeleteView(views.View):
    def get(self, request, pelicula_id):
        pelicula = Pelicula.objects.get(id=pelicula_id)
        pelicula.delete()
        return redirect('peliculas:movie_list')