from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    code = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.name

class City(models.Model):
    TIRES_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
    ]
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities', null=True, blank=True)
    tire = models.PositiveSmallIntegerField(choices=TIRES_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

# class Location(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, null=True, blank=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='locations', null=True, blank=True)
#     lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     radious_km = models.PositiveIntegerField(null=True, blank=True)
#     geohash = models.CharField(max_length=12, null=True, blank=True)

#     def __str__(self):
#         return f"{self.name}, {self.city}, {self.country}"