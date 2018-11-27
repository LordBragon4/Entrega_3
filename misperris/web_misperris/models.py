from django.db import models

# Create your models here.
class Rescatado(models.Model):
    foto = models.ImageField(upload_to='./media/imagenes/')#RUTA DE IMAGENES 
    nombre = models.CharField(max_length=30, primary_key=True)
    raza = models.CharField(max_length=30)
    descr = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=30,default="Rescatado", choices=(('Rescatado','Rescatado'),('Disponible','Disponible'),('Adoptado','Adoptado')))

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    correo = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    run = models.IntegerField(primary_key=True)
    tipo_usuario = models.CharField(max_length=20, null=True)
    nombre = models.CharField(max_length=15)
    snombre = models.CharField(max_length=15)
    paterno = models.CharField(max_length=15)
    materno = models.CharField(max_length=15)
    fnac = models.DateTimeField()
    telefono = models.IntegerField()
    region = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    vivienda = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.nombre


