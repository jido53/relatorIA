from django.db import models
from django.contrib.auth.models import User


class Jurisdiction(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre del fuero

    def __str__(self):
        return self.name

class CaseType(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre del tipo de caso

    def __str__(self):
        return self.name

class Case(models.Model):
    jurisdiction = models.ForeignKey(Jurisdiction, on_delete=models.CASCADE, related_name='cases')  # Fuero
    description = models.TextField()  # Descripción breve del caso
    case_type = models.ForeignKey(CaseType, on_delete=models.CASCADE, related_name='cases')  # Tipo de proceso o caso
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cases')  # Usuario que creó el caso
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    current_stage = models.ForeignKey('Stage', on_delete=models.SET_NULL,blank=True, null=True)  # Etapa actual del caso

    def __str__(self):
        return f"{self.jurisdiction} - {self.description[:20]}..."

class Document(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')  # Ruta de almacenamiento del archivo
    uploaded_at = models.DateTimeField(auto_now_add=True)
    stage = models.ForeignKey('Stage', on_delete=models.SET_NULL,blank=True, null=True)  # Etapa del proceso en la que se encuentra el documento

    def __str__(self):
        return self.title

class Stage(models.Model):
    name = models.CharField(max_length=100)  # Nombre de la etapa (ej. "Audiencia", "Sentencia")
    description = models.TextField(blank=True)  # Descripción opcional
    is_key_stage = models.BooleanField(default=False)  # Si es una etapa clave o de transición

    def __str__(self):
        return self.name
        
class EntityType(models.Model):
    name = models.CharField(max_length=50)  # Nombre del tipo de entidad (e.g., "Nombre", "Fecha", "Monto")
    description = models.TextField(blank=True)  # Descripción opcional del tipo de entidad

    def __str__(self):
        return self.name
        
class Entity(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='entities')
    entity_type = models.ForeignKey(EntityType, on_delete=models.CASCADE)  # Referencia al modelo EntityType
    value = models.TextField(blank=True)  # Valor de la entidad (e.g., el nombre o fecha específicos)
    description = models.TextField(blank=True)  # Descripción de la entidad
    parent_entity = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_entities')

    def __str__(self):
        return f"{self.entity_type.name}: {self.value}"

class Summary(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE, related_name='summary')
    content = models.TextField(blank=True)  # Contenido del resumen generado por IA
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    edited_by_user = models.BooleanField(default=False)  # Si el usuario editó el resumen

    def __str__(self):
        return f"Summary for {self.document.title}"



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)  # Área a la que pertenece el usuario
    role = models.CharField(max_length=50, choices=[('Lawyer', 'Abogado'), ('Paralegal', 'Paralegal'), ('Admin', 'Administrativo')])

    def __str__(self):
        return f"{self.user.username} - {self.role}"