from django.db import models
from account.models import User
from django.utils.text import slugify
from business.utils import generate_biz_id

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', limit_choices_to={'level': 0})
    level = models.PositiveIntegerField(default=0)

    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, null=True, blank=True)
    home_order = models.PositiveIntegerField(default=0, null=True, blank=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    

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