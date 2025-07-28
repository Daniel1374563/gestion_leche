from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    cantidad_de_litros = models.DecimalField(max_digits=10, decimal_places=2)
    numero_de_telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_de_entrega = models.CharField(max_length=20, help_text="Día de la semana para la entrega")
    importe_a_pagar = models.DecimalField(max_digits=10, decimal_places=2)

    done = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
