from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Access_level, Garage, Work_order, Service_schedule,Fault, Maintenance_type, Vehicle, Vehicle_type, Vehicle,Tyre, Maintenance_record, Staff, Garage_manager

# These are my registered models and how they are to appear on the admin page

#Registering the Access_level model
@admin.register(Access_level)
class Access_levelAdmin(admin.ModelAdmin):
    list_display=(
        'Access_Level_ID',
        'Description'
    )
#admin.site.register(Access_level, Access_levelAdmin)


#Registering the Staff model
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display =(
        'id',
        'first_name',
        'last_name',
        'username',
        'password',
        'email',
        'PhoneNo',
        'Access_Level_ID',
        #'Responsibility'
    )
#admin.site.register(Staff, StaffAdmin)


#Registering the Garage model
@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    list_display=(
        'GarageID',
        'GarageName',
        'Address',
        'WorkOrderNo',
        'PersonID'
    
    ) 
#admin.site.register(Garage, GarageAdmin)


#Registering the Garage_manager model 
#@admin.register(Garage_manager)
#class Garage_managerAdmin(admin.ModelAdmin):
    #list_display=(
        #'PersonID',
        #'FName',
        #'LName',
        #'UserName',
        #'Password',
        #'email',
        #'PhoneNo',
        #'Responsibility',
        #'Access_Level_ID',
    #)
#admin.site.register(Garage_manager, Garage_managerAdmin)


#Registering the Work_order model
@admin.register(Work_order)
class Work_orderAdmin(admin.ModelAdmin):
    list_display= (
        'WORK_ORDER_id',
        'Date_of_Creation',
        'Date_of_Approval',
        'Estimated_Cost',
        'Date_of_Completion',
        'Garage_Name',
        'PersonID',
        'MAINTENANCE_TYPE_id'
    )
#admin.site.register(Work_order, Work_orderAdmin)

#Registering the Service_schedule model
@admin.register(Service_schedule)
class Service_scheduleAdmin(admin.ModelAdmin):
    list_display= (
        'Schedule_id',
        'Year',
        'Service_Mileage',
        'Service_Items',
        'Level_code',
        'Plate_Number',
    )
#admin.site.register(Service_schedule, Service_scheduleAdmin)


#Registering the Fault model
@admin.register(Fault)
class FaultAdmin(admin.ModelAdmin):
    list_display=(
        'Fault_id',
        'Description',
        'Date_of_Occurence',
        'Fault_Status',
        'Plate_Number',
        'PersonID'
    )
#admin.site.register(Fault, FaultAdmin)


#Registering the Maintenance_type models
@admin.register(Maintenance_type)
class Maintenance_typeAdmin(admin.ModelAdmin):
    list_display=(
        'Maintenance_Type_ID',
        'Fault_id',
        'Schedule_id',
        'Description'
    )
#admin.site.register(Maintenance_type, Maintenance_typeAdmin)


#Registering the Vehicle model
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display=(
        'Plate_Number',
        #'VIN',
        #'Plate_No',
        'Make',
        'Model',
        'Year',
        'Colour',
        'Vehicle_Description',
        'Put_in_service_Date',
        'Taken_out_of_service_Date',
        'Current_Mileage',
        'Engine_Oil_Change_Mileage',
        'Interim_service_Mileage',
        'Full_service_Mileage',
        #'Tire_Size',
        'Down_Time',
        #'Service_Interval',
        'PersonID',
        'VEHICLE_TYPE_id'
    )
#admin.site.register(Vehicle, VehicleAdmin)


#Registering the Vehicle_type model
@admin.register(Vehicle_type)
class Vehicle_typeAdmin(admin.ModelAdmin):
   list_display=(
        'Vehicle_Type_ID',
        'Description'
    )
#admin.site.register(Vehicle_type, Vehicle_typeAdmin)


#Registering the Tyre model to appear on the admin portal
@admin.register(Tyre)
class TyreAdmin(admin.ModelAdmin):
    list_display=(
        'Tyre_code',
        'Plate_Number',
        'Tyre_model',
        'Tyre_brand',
        'Tyre_size',
        'Tread_depth',
        'Tyre_description',
        'Load_capacity',
        'Material',
        'Rim_width',
        'Section_width',
        'Radius',
        'Speed_rating',
        'Wear_and_tear',
        'Tyre_service_mileage',
    )
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "username")
    
    def get_fieldsets(self, request, obj=None, **kwargs):
        fieldsets = super().get_fieldsets(request, obj=obj, **kwargs)
        fieldsets += (('Permissions',{'fields': ('groups', 'user_permissions')})),
        return fieldsets
    
#Registering the Maintenance_record model on the admin portal
@admin.register(Maintenance_record)
class Maintenance_recordAdmin(admin.ModelAdmin):
    list_display=(
        'Maintenance_record_id',
        'Start_date',
        'Completion_date',
        'Description_of_Maintenance_actions',
        'Maintenance_cost',
        'Maintenance_Status',
        'Maintenance_type_ID',
        'WORK_ORDER_id',
        'Plate_Number',
        'PersonID'
    )


#admin.site.unregister(UserAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.register(Group)
