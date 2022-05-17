from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5,decimal_places=2)