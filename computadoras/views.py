from django.shortcuts import render, redirect
from django import views
from .models import ComputadoraModel
from .forms import ComputadoraForm


class LandingView(views.View):
    def get(self, request):

        hola = "Bienvenido(a) a las computadoras"
        template_name = "computadoras/landing.html"
        context = {
            'saludo':hola
        }
        return render(request, template_name, context)


class ListView(views.View):
    def get(self, request):

        template_name = "computadoras/lista.html"
        computadoras = ComputadoraModel.objects.all()
        context = {
            'computadoras':computadoras
        }
        return render(request, template_name, context)


class DetailView(views.View):
    def get(self, request, computer_id):

        template_name = "computadoras/detalle.html"
        computadora = ComputadoraModel.objects.get(id=computer_id)
        prefijo = "GB"
        if computadora.hardDisk / 1024 >= 1:
            computadora.hardDisk = computadora.hardDisk/1024
            prefijo = "TB"
        context = {
            'computadora': computadora,
            'prefijo':prefijo
        }
        return render(request, template_name, context)


class CreateView(views.View):
    def get(self, request):

        template_name = "computadoras/createform.html"
        form = ComputadoraForm()
        context = {
            'form':form,
            'type':'create'
        }

        return render(request, template_name, context)

    def post(self, request):

        new_form = ComputadoraForm(request.POST, request.FILES)

        if new_form.is_valid():
            form_data = new_form.save(commit=False)
            form_data.save()

            return redirect('computadoras:list')

        else:
            template_name = "computadoras/createform.html"
            form = ComputadoraForm()
            error = "El formulario no es valido"

            context = {
                'form':form,
                'error':error,
                'type': 'create'
            }

            return render(request, template_name, context)


class EditView(views.View):
    def get(self, request, computer_id):
        template_name="computadoras/createform.html"
        computer = ComputadoraModel.objects.get(id=computer_id)
        form = ComputadoraForm(instance=computer)
        context = {
            'form':form,
            'type': 'edit',
            'computer':computer
        }
        return render(request, template_name, context)

    def post(self, request, computer_id):
        computer = ComputadoraModel.objects.get(id=computer_id)
        form_edit = ComputadoraForm(request.POST, request.FILES, instance=computer)

        if form_edit.is_valid():
            form_data = form_edit.save(commit=False)
            form_data.save()

            return redirect('computadoras:detail', computer.id)
        else:
            template_name = "computadoras/createform.html"
            computer = ComputadoraModel.objects.get(id=computer_id)
            form = ComputadoraForm(instance=computer)
            error = "El formulario no es valido"
            context = {
                'form': form,
                'error':error,
                'type': 'edit',
                'computer': computer
            }
            return render(request, template_name, context)


class DeleteView(views.View):
    def get(self, request, computer_id):
        computer = ComputadoraModel.objects.get(id=computer_id)
        computer.delete()
        return redirect('computadoras:delete')
