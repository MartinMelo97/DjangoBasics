from django.db import models

sexo = (
    ('Masculino', 'Hombre'),
    ('Femenino', 'Mujer')
)


class Director(models.Model):
    nombre = models.CharField(max_length=140)
    fecha_nacimiento = models.DateField()
    imagen = models.ImageField(upload_to="images/peliculas/directores")
    sexo = models.CharField(max_length=140, choices=sexo)

    def __str__(self):
        return self.nombre


class Actor(models.Model):
    nombre = models.CharField(max_length=140)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=140, choices=sexo)
    imagen = models.ImageField(upload_to="images/peliculas/actores")

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=140)
    duracion = models.DurationField()
    sinopsis = models.TextField()
    portada = models.ImageField(upload_to="images/peliculas")
    estreno = models.BooleanField(default=False)
    director = models.ForeignKey(Director, related_name="peliculas", on_delete=models.CASCADE)
    actores = models.ManyToManyField(Actor, related_name="peliculas")

    def __str__(self):
        return self.titulo
