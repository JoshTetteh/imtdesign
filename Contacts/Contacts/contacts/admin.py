from django.contrib import admin

# Register your models here.

from .models import Staff
from .models import Position
from. models import Posted
from. models import Activities
from. models import Address
from. models import MnEStaff
from. models import Engagement
"""admin.site.register(Activities)
admin.site.register(Address)
admin.site.register(MnEStaff)
admin.site.register(Engagement)
admin.site.register(Position)
admin.site.register(Staff)
admin.site.register(Posted) """

@admin.register(Posted)
class PostedAdmin(admin.ModelAdmin):
    list_display = ["Name",  "Date", "Designation", "Location"] 
    ordering = ["Location"]
    search_fields =["Name", "Designation", "Location","Date"] 

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["Designation", "Superior", "Direct_Report", "Location"] 
    ordering = ["Designation"]
    search_fields = ("Location","Designation")

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display =["Name", "Phone_no", "Email"]
    search_fields = ["Name"]
    ordering =["Name"]

@admin.register(Engagement)
class EngagementAdmin(admin.ModelAdmin):
    list_display = ["Engagement_Name", "Engagement_Type", "Description", "Department"]
    search_fields =["Engagement Name"]
    ordering = ["Department"]

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["Department", "Company", "Physical_Address"]
    search_fields =["Department","Company", "Physical_Address"]
    ordering = ["Company"]

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ["Engagement_Name", "Name", "Department", "Due_Date", "Date_completed"]
    search_fields = ["Engagement_Name", "Name", "Department"]
    ordering = ["Engagement_Name"]

@admin.register(MnEStaff)
class MnEStaffAdmin(admin.ModelAdmin):
    list_display =["Name", "Email", "Phone_Number"]
    search_fields =["Name"]
    ordering = ["Name"]