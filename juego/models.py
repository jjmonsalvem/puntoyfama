from django.db import models

# Create your models here.
class Partida(models.Model):
    numero_generado = models.CharField(max_length=4)  # Número aleatorio de 4 dígitos
    fecha_inicio = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    completada = models.BooleanField(default=False)  # Si la partida terminó

    def __str__(self):
        return f"Partida {self.id} - {self.numero_generado}"
    

class Intento(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)  # Relación con la partida
    numero_ingresado = models.CharField(max_length=4)  # Número que ingresó el usuario
    puntos = models.IntegerField()  # Dígitos en la posición correcta
    famas = models.IntegerField()  # Dígitos en la posición incorrecta
    fecha_intento = models.DateTimeField(auto_now_add=True)  # Fecha y hora del intento

    def __str__(self):
        return f"Intento {self.numero_ingresado} - Puntos: {self.puntos}, Famas: {self.famas}"
    
class Juego(models.Model):
    nombre = models.CharField(max_length=100)


