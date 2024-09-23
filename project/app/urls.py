from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Home views and Dashboard. Both '/' and '/home/' path is same, we made two path for convenience 
    path('', views.home, name='home'),
    path('home/', views.home, name = 'home'),
    
    # Authentication views (Register, Login, Logout, Register as Volunteer)
    path('register/', views.register, name = 'register'),
    path('register/volunteer/', views.register_volunteer, name = 'register_volunteer'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    
    # Basic web application pages to manage and see donation, crisis, volunteer, and managing inventory such as add, update and delete operations
    path('donation/', views.donation, name = 'donation'),
    path('crisis/', views.crisis, name = 'crisis'),
    path('volunteer/', views.volunteer, name = 'volunteer'),
    path('inventory/', views.list_inventory, name = 'list_inventory'),
    path('inventory/add/', views.add_inventory, name = 'add_inventory'),
    path('inventory/update/<int:pk>/', views.update_inventory, name = 'update_inventory'),
    path('inventory/delete/<int:pk>/', views.delete_inventory, name = 'delete_inventory'),
    
    # profile section for volunteers 
    path('account/', views.profile_view, name = 'profile'),
    
    # admin section for management and updates
    path('admin_panel/volunteer/', views.admin_volunteer, name = 'admin_volunteer'),
    path('admin_panel/crisis/', views.admin_crisis, name = 'admin_crisis'),
    path('admin_panel/crisis/approve/<int:crisis_id>/', views.admin_approve_crisis, name = 'approve_crisis'),
    path('admin_panel/crisis/update/<int:crisis_id>/', views.admin_update_crisis, name = 'update_crisis'),
]


# Basic Django code for Media routing 
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)