from django.db import models

class AttributeType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Attribute(models.Model):
    type = models.ForeignKey(AttributeType, on_delete=models.CASCADE, related_name='attributes')
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('type', 'value')

    def __str__(self):
        return f"{self.type.name}: {self.value}"
    