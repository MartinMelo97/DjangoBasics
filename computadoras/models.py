from django.db import models


class ComputadoraModel(models.Model):

    #tupla
    procesadores = (
        ('Intel i3', 'Intel - i3'),
        ('Intel i5', 'Intel - i5'),
        ('Intel i7', 'Intel - i7'),
        ('AMD A6', 'AMD - A6'),
        ('AMD A8', 'AMD - A8'),
        ('AMD A10', 'AMD - A10'),
    )

    marca = models.CharField(max_length=140)
    modelo = models.CharField(max_length=50)
    RAM = models.PositiveIntegerField()
    hardDisk = models.PositiveIntegerField()
    procesador = models.CharField(max_length=140, choices=procesadores)
    imagen = models.ImageField(upload_to='images/computers')

    def __str__(self):
        return self.marca + ' ' + self.modelo