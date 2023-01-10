from django.db import models

#creamos los modelos y una vez terminemos de crearlos 
#ejecutamos el comando "python manage.py makemigrations" 
#esto para preparar los cambios en la base de datos
#luego el comando "python manage.py migrate" para confirmar los cambios
class Director(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField(null= True, blank = True)
    biografia = models.TextField()
    imagen = models.URLField()

    def __str__(self):
        return self.nombre + " " + self.apellidos 

class Pelicula(models.Model):
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25)
    sinopsis = models.TextField()
    duracion = models.PositiveIntegerField()
    imagen = models.URLField()
    anyo = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
