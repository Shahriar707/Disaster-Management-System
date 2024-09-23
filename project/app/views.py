# importing necessary libraries, modules, files, models, forms that are necessary to write view functions

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout 
from django.urls import reverse
from .models import Donation, Crisis, Volunteer, Inventory
from django.db.models import Sum
from .forms import DonationForm, CrisisForm, VolunteerForm, InventoryForm, VolunteerProfileForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

# Create your views here.

# Home function that shows the dashboard where, total donation amount, list of recent crisis and available volunteers are shown
def home(request):
    total_funds = Donation.objects.aggregate(Sum('amount'))['amount__sum'] or 0 
    recent_crisis = Crisis.objects.order_by('-date')[:5]
    available_volunteers = Volunteer.objects.filter(is_available=True)
    
    context = {
        'total_funds' : total_funds,
        'recent_crisis' : recent_crisis,
        'available_volunteers': available_volunteers
    }
    
    return render(request, 'home.html', context)


# registering new user that redirects to the registering as a volunteer page
# It uses UserCreationForm that includes built in Django User model, so that without creating any user form or model we can register user 
def register(request):
    if request.method == "POST": 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            user = form.save(commit=False)
            user.is_staff = True 
            user.save()
            login(request, user)
            return redirect(reverse(("register_volunteer")))
    else:
        form = UserCreationForm()
    return render(request, "register.html", { "form": form })


# view function to registering new volunteers and it used VolunteerForm and Volunteer Model
def register_volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            vol = form.save(commit=False)
            vol.user = request.user 
            vol.name = request.user.username 
            vol.save()
            return redirect('login')
    else:
        form = VolunteerForm()
        
    return render(request, 'register_volunteer.html', {'form' : form})


# After registering as an user, this view function helps user to validate and login to the system
def login_view(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            return redirect("home")
    else: 
        form = AuthenticationForm()
    return render(request, "login.html", { "form": form })


# logout view function 
def logout_view(request):
    logout(request)
    
    return redirect('login')


# Donation view function uses Donation Model and DonationForm to update and add new Donation and shows the total donation amount too
# If it's a POST request then it will send the form with submitted data or if it's a GET request, then it will show a new form
# Anyone can view this page, no authorization needed
def donation(request):
    total_funds = Donation.objects.aggregate(Sum('amount'))['amount__sum'] or 0 
    donations = Donation.objects.all().order_by('-date')
    
    form = DonationForm()
    
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            if request.user.is_authenticated():
                donation.user = request.user
            donation.save()
            return redirect('donation')
    else:
        form = DonationForm()     
        
    context = {
        'total_funds' : total_funds,
        'donations': donations,
        'form' : form
    }       
    
    return render(request, 'donation.html', context)


# Crisis view function uses Crisis Model and CrisisForm to update and add new Crisis and shows the list of Crisis too
# If it's a POST request then it will send the form with submitted data or if it's a GET request, then it will show a new form
# Anyone can view this page, no authorization needed
def crisis(request):
    recent_crisis = Crisis.objects.filter(is_approved=True)
    
    severity_filter = request.GET.get('severity')
    if severity_filter:
        crisis = Crisis.objects.filter(severity = severity_filter)
    
    form = CrisisForm()
    
    if request.method == 'POST':
        form = CrisisForm(request.POST)
        if form.is_valid():
            crisis = form.save(commit=False)
            crisis.is_approved = False 
            crisis.save()
            return redirect('crisis')
    else:
        form = CrisisForm()
    
    return render(request, 'crisis.html', {'recent_crisis' : recent_crisis, 'form' : form})


# Volunteer view function uses Volunteer Model and shows the list of Volunteer too
# It's a GET request, and anyone can view this page, no authorization needed
def volunteer(request):
    volunteers = Volunteer.objects.all()
    
    return render(request, 'volunteers.html', {'volunteers' : volunteers})


# add_inventory view function uses Inventory Model and InventoryForm to add new inventory items and shows the list and amount of inventory items
# If it's a POST request then it will send the form with submitted data or if it's a GET request, then it will show a new form
# Anyone can view this page, but login is required. That's why I used login required decorators and check if user is a staff or a volunteer
@login_required
def add_inventory(request):
    if not request.user.is_staff and not hasattr(request.user, 'volunteer'):
        return redirect('home')
    
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory_item = form.save(commit=False)
            inventory_item.added_by = request.user 
            inventory_item.save()
            return redirect('list_inventory')
    else:
        form = InventoryForm()
    
    return render(request, 'add_inventory.html', {'form' : form})


# update_inventory view function uses Inventory Model and InventoryForm to update any inventory items's parameters and fields 
# If it's a POST request then it will send the form with submitted data or if it's a GET request, then it will show a new form
# it uses pk as primary key or pk to access the item
# Anyone can view this page, but login is required. That's why I used login required decorators and check if user is a staff or a volunteer
@login_required
def update_inventory(request, pk):
    inventory_item = get_object_or_404(Inventory, pk=pk)
    
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory_item)
        if form.is_valid():
            form.save()
            return redirect('list_inventory')
    else:
        form = InventoryForm(instance=inventory_item)
        
    return render(request, 'update_inventory.html', {'form' : form})


# delete_inventory view function uses Inventory Model and InventoryForm to delete any inventory items 
# If it's a POST request then it will send the form with submitted request and deletes the item
# it uses pk as primary key or pk to access the item
# Anyone can view this page, but login is required. That's why I used login required decorators and check if user is a staff or a volunteer
@login_required
def delete_inventory(request, pk):
    inventory_item = get_object_or_404(Inventory, pk=pk)

    if request.method == 'POST':
        inventory_item.delete()
        return redirect('list_inventory')
    
    return render(request, 'delete_inventory.html', {'item' : inventory_item})


# list_inventory view function uses Inventory Model to show the list of all inventory items
# It's a GET request, Anyone can view this paged while being logged in
@login_required
def list_inventory(request):
    inventory_items = Inventory.objects.all()
    
    return render(request, 'list_inventory.html', {'inventory_items' : inventory_items})


# profile_view function uses Volunteer Model and VolunteerProfileForm to create a profile section for users and volunteers 
# Login is required to access this page 
@login_required
def profile_view(request):
    user = request.user 
    
    try:
        volunteer = user.volunteer
    except Volunteer.DoesNotExist:
        volunteer = None 
        
    if request.method == 'POST':
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        
        user.save()
        
        if volunteer:
            volunteer_form = VolunteerProfileForm(request.POST, instance=volunteer)
            
            if volunteer_form.is_valid():
                volunteer_form.save()
        else:
            volunteer_form = VolunteerProfileForm()
            
        return redirect('profile')
    
    else:
        volunteer_form = VolunteerProfileForm(instance=volunteer) if volunteer else None 
        
    context = {
        'user' : user,
        'volunteer_form' : volunteer_form
    }
    
    return render(request, 'account.html', context)


# admin_volunteer view function manages volunteer section where admin can view the list of volunteers 
# one needs to a super user or staff member to access this page
@staff_member_required
def admin_volunteer(request):
    volunteers = Volunteer.objects.all()
    
    return render(request, 'admin_volunteer.html', {'volunteers' : volunteers})


# admin_crisis view function manages crisis section where admin can view the list of recent crisis 
# one needs to a super user or staff member to access this page
@staff_member_required
def admin_crisis(request):
    recent_crisis = Crisis.objects.all()
    
    return render(request, 'admin_crisis.html', {'crises' : recent_crisis})


# admin_approve_crisis view function lets an admin can to approve a pending crisis post on the website
# one needs to a super user or staff member to access this page
@staff_member_required
def admin_approve_crisis(request, crisis_id):
    crisis = get_object_or_404(Crisis, id=crisis_id)
    crisis.is_approved = True 
    crisis.save()
    
    return redirect('admin_crisis')


# admin_update_crisis view function lets an admin update the status of a existing or pending crisis 
# one needs to a super user or staff member to access this page
@staff_member_required
def admin_update_crisis(request, crisis_id):
    
    if request.method == 'POST':
        crisis = get_object_or_404(Crisis, id=crisis_id)
        status = request.POST.get('status')
        crisis.status = status
        crisis.save()
        
        return redirect('admin_crisis')