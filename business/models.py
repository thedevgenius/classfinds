from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories', limit_choices_to={'level': 0})
    level = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.parent:
            self.level = self.parent.level + 1
        else:
            self.level = 0
        super().save(*args, **kwargs)

# class Business(models.Model):
#     biz_id = models.CharField(max_length=20, unique=True)
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, null=True, blank=True)
#     tagline = models.CharField(max_length=255, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)

#     address = models.TextField()
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField(unique=True)
#     website = models.URLField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name