from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donation(models.Model):
    donor_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.donor_name} - {self.amount}'
    
    
class Crisis(models.Model):
    status = [
        ('open', 'open'),
        ('closed', 'closed'),
        ('pending', 'pending')
    ]
    severity = [
        ('low', 'low'), 
        ('medium', 'medium'), 
        ('high', 'high')
    ]    
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    severity = models.CharField(max_length=10, choices=severity)
    status = models.CharField(max_length=10, choices=status, default='pending')
    date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    required_help = models.TextField(max_length=300, default='Not Specified')
    images = models.ImageField(upload_to='photos/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    assigned_task = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Inventory(models.Model):
    Inventory_types = [('Relief', 'Relief'), ('Expenses', 'Expenses')]
    
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    inventory_type = models.CharField(max_length=100, choices=Inventory_types)
    description = models.TextField(blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.item_name
    

# The models.py has four models name Donation, Crisis, Volunteer, Inventory
# Each of the models has basic fields like title, name, date and time
# Each of the models has also some fields that are related to their fields like the amount in case of donation, description in terms of crisis and inventory
# All of the models are reuseable components  