from django import forms 
from .models import Donation, Crisis, Volunteer, Inventory

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount']
        
        
class CrisisForm(forms.ModelForm):
    class Meta:
        model = Crisis 
        fields = ['title', 'location', 'description', 'severity', 'status', 'images', 'required_help']
        

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['age', 'phone_number', 'is_available', 'assigned_task']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'assigned_task': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'quantity', 'inventory_type', 'description']
        
        
class VolunteerProfileForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['age', 'phone_number', 'is_available', 'assigned_task']
        
        
        
# The forms.py to define forms that collect and validate user input based on the models created in the models.py 
# I have created 5 forms for donation, crisis, inventory, volunteer and volunteer profile
# VolunteerForm is used to create the Volunteer page while the VolunteerProfileForm is used to create the profile page 
# Each of the forms can be termed as reuseable components 