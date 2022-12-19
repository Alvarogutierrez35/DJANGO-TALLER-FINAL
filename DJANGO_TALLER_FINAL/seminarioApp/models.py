from django.db import models
from django.utils import timezone
opciones_estado = [    
    ("Reservado", "Reservado"),    
    ("Completada", "Completada"),    
    ("Anulada", "Anulada"),    
    ("No asisten", "No asisten")]

instituciones = [    
    ("U Catolica", "U Catolica"),    
    ("U de Chile", "U de Chile"),    
    ("UFRO", "UFRO"),    
    ("Santo Tomas", "Santo Tomas"),    
    ("U Autonoma", "U Autonoma"),    
    ("Inacap", "Inacap"),    
    ("AIEP", "AIEP")]

# Create your models here.
class Inscrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fechaInscripcion = models.DateField()
    institucion = models.CharField(max_length=50, choices=instituciones)
    horaInscripcion = models.TimeField()
    estado = models.CharField(max_length=50, choices=opciones_estado)
    observacion = models.CharField(max_length=50)


    def save(self, *args, **kwargs):
        if not self.id:
            self.fechaInscripcion = timezone.now().date()
            self.horaInscripcion = timezone.now().time()
        super(Inscrito, self).save(*args, **kwargs)
    @property
    def fecha_inscripcion_formateada(self):
        return self.fechaInscripcion.strftime("%d/%m/%Y")
    def hora_inscripcion_formateada(self):
        return self.horaInscripcion.strftime("%H:%M")

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    institucion = models.CharField(max_length=50)