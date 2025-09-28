from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Discipline(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Adicione unique=True aqui
    # ... outros campos ...
    
    class Meta:
        # REMOVA ou CORRIJA a linha unique_together se estiver incorreta
        # unique_together = ['name']  # Isso deve ser removido se name já for unique
        pass
    
    def __str__(self):
        return self.name