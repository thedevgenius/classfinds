from django.db import models
from account.models import User
from django.utils.text import slugify
from .utils import generate_biz_id

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

class Business(models.Model):
    biz_id = models.CharField(max_length=20, unique=True, null=True, blank=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='businesses')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='businesses')
    categories = models.ManyToManyField(Category, related_name='related_businesses', blank=True)

    phone = models.CharField(max_length=20, blank=True, null=True)
    alternate_phone = models.CharField(max_length=20, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    image = models.ImageField(upload_to='business_images/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Businesses"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.biz_id:
            self.biz_id = generate_biz_id()

        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Business.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)