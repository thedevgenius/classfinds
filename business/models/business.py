from django.db import models
from account.models import User
from django.utils.text import slugify
from business.utils import generate_biz_id
from .category import Category
from .location import Location
from .attribute import Attribute


class Business(models.Model):
    biz_id = models.CharField(max_length=20, unique=True, null=True, blank=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='businesses')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='businesses')
    categories = models.ManyToManyField(Category, related_name='related_businesses', blank=True)
    year_of_est = models.IntegerField(null=True, blank=True)

    phone = models.CharField(max_length=20, blank=True, null=True)
    alternate_phone = models.CharField(max_length=20, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    image = models.ImageField(upload_to='business_images/', blank=True, null=True)

    attributes = models.ManyToManyField('Attribute', blank=True, related_name='businesses')

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