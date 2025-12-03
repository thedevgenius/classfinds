from django.db import models

# Create your models here.
class Lead(models.Model):
    LEAD_SOURCE_CHOICES = [
        ('RDB', 'Road Banner'),
        ('FBG', 'Facebook Group'),
        ('JSD', 'Justdial'),
        ('WAP', 'Whatsapp'),
        ('OTH', 'Other'),
    ]
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('CON', 'Contacted'),
        ('INT', 'Interested'),
        ('NOT', 'Not Interested'),
        ('CAN', 'Cancelled'),
        ('JND', 'Joined'),
        ('OTH', 'Other'),
    ]
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    is_received = models.BooleanField(default=False)
    source = models.CharField(max_length=3, choices=LEAD_SOURCE_CHOICES, default='OTH')
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='NEW')
    is_added = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"