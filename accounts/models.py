from django.db import models
#import uuid

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractUser

#This is the Access Level model
class Access_level(models.Model):
    Access_Level_ID = models.AutoField(primary_key=True, null=False, db_column='Access_Level_id')
    Description = models.CharField(max_length=50, db_column='Description')
    
    class Meta:
        db_table = 'ACCESS_LEVEL'
        ordering = ('Access_Level_ID',)
    
    def __str__(self):
        return self.Description

#Customizing the User model and Naming it Person
class CustomUser(AbstractUser):
    id = None
    password = None
    id = models.BigAutoField(primary_key=True, unique=True,db_column='id')
    email = models.EmailField(unique=True, blank=False, null=False, db_column='email')
    password = models.CharField(max_length=256, blank=False, null=False, db_column='password',write_only=True)
    first_name = models.CharField(max_length=20, blank=False, null=False, db_column='FName')
    last_name = models.CharField(max_length=20, blank=False, null=False, db_column='LName')
    username = models.CharField(max_length=20,db_column='UserName', unique=True, blank=False, null=False)
    PhoneNo = models.CharField(max_length=45,default=0, db_column='PhoneNo')
    Access_Level_ID = models.OneToOneField(Access_level, models.DO_NOTHING, db_column='Access_Level_ID', blank=True, null=True)
    groups= models.ManyToManyField('auth.Group',related_name='user_set', related_query_name='user', blank=True,db_column='Responsibility',null=False, verbose_name='groups')
    is_superuser = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta(AbstractUser.Meta):
        ordering = ('id',)
    def __str__(self):
        return self.FName and self.LName
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }


class Person(CustomUser):
    class Meta(CustomUser.Meta):
        db_table = 'PERSON'
        ordering = ('id',)
        
    def __str__(self):
        return self.FName and self.LName

    
#This was an abstract model to be inherited by the Garage manager and the staff models but has been replaced by the Person model that is a custom user model
#class Person(models.Model):
    #PersonID = models.AutoField(primary_key=True, db_column='Person_id', unique=True)
    #FName = models.CharField(max_length=20,db_column='FName')
    #LName = models.CharField(max_length=20,db_column='LName')
    #UserName = models.CharField(max_length=20,db_column='UserName')
    #Password = models.CharField(max_length=20, db_column='Password')
    #Address = models.CharField(max_length=45, db_column='Address')
    #email = models.CharField(max_length=45, db_column='Email')
    #PhoneNo = models.IntegerField(default=0, db_column='PhoneNo')
    #Access_Level_ID = models.OneToOneField(Access_level, models.DO_NOTHING, db_column='Access_Level_ID', blank=True, null=True)  # Field name made lowercase.
    #Responsibility= models.OneToOneField('auth.Group', related_name='user_set', related_query_name='user', blank=True,db_column='Responsibility',null=False, on_delete=models.CASCADE)

    #class Meta:
        #db_table = 'PERSON'
        #ordering = ('PersonID',)
        #abstract = True
        
    #def __str__(self):
        #return self.FName and self.LName
    

#This is the Garage_manager model that inherits atributes from the Person Model   
class Garage_manager(Person):
    
    class Meta(Person.Meta):
        db_table = 'GARAGE_MANAGER'
        ordering = ('id',)
    
    def __str__(self):
        return self.FName and self.LName
    
        
#This is the Garage model that creates table to store information about the Garages
class Garage(models.Model):
    GarageID = models.AutoField(primary_key=True)
    GarageName = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    WorkOrderNo = models.IntegerField(default=0)
    PersonID = models.ForeignKey(Person, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        db_table = 'GARAGE'
        ordering = ('GarageID',)
    
    def __str__(self):
        return self.GarageName

#Staff model inherits the person model but specialises on the specific internal staff
class Staff(Person):
    
    class Meta(Person.Meta):
        db_table = 'STAFF'
        ordering = ('id',)
        verbose_name_plural ='Staff'
    
    def __str__(self):
        return self.FName and self.LName

#Vehilce_type model to store the vehilce types and descriptions
class Vehicle_type(models.Model):
    Vehicle_Type_ID = models.AutoField(primary_key=True, db_column='Vehicle_Type_ID', unique=True)
    Description = models.CharField(max_length=30, db_column='Description')
    
    class Meta:
        db_table = 'VEHICLE_TYPE'
        ordering = ('Vehicle_Type_ID',)
    
    def __str__(self):
        return self.Description

#Vehicle model to store information on particular vehicles 
class Vehicle(models.Model):
    #Vehicle_id = models.IntegerField(primary_key=True, db_column='Vehicle_id', unique=True)
    #VIN = models.CharField(max_length=45, db_column='VIN')
    Plate_Number = models.CharField(primary_key=True,max_length=20, db_column='Plate_Number')
    Make = models.CharField(max_length=30, db_column='Make')
    Model= models.CharField(max_length=30, db_column='Model')
    Year = models.DateField(db_column='Year')
    Current_location = models.CharField(max_length=50, db_column='Current_location')
    Colour = models.CharField(max_length=20, db_column='Colour')	
    Vehicle_Description = models.TextField(max_length=500, db_column='Vehicle_Description')
    Put_in_service_Date = models.DateTimeField(db_column='Put_in_service_Date')
    Taken_out_of_service_Date = models.DateTimeField(db_column='Taken_out_of_service_Date')
    Intial_Mileage = models.CharField(max_length=20,db_column='Intial_Mileage',default = 0)
    Current_Mileage = models.CharField(max_length=20,db_column='Current_Mileage')
    Engine_Oil_Change_Mileage = models.CharField(max_length=20,db_column='Engine_Oil_Change_Mileage')
    Interim_service_Mileage = models.CharField(max_length=20,db_column='Interim_service_Mileage')
    Full_service_Mileage = models.CharField(max_length=20,db_column='Full_service_Mileage')
    #Tire_Size = models.IntegerField(db_column='Tire_Size')
    Down_Time = models.CharField(max_length = 20, db_column='Down_Time')
    #Service_Interval = models.IntegerField(db_column='Service_Interval')
    PersonID = models.ForeignKey(Person, related_name='PERSON_PERSON_id', on_delete=models.CASCADE, db_column='PersonID', blank=True, null=True)  
    VEHICLE_TYPE_id = models.ForeignKey(Vehicle_type, models.DO_NOTHING, db_column='VEHICLE_TYPE_id', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        ordering = ['Put_in_service_Date', 'Taken_out_of_service_Date']
        db_table = 'VEHICLE'
    
    def __str__(self):
        return self.VIN and self.Plate_No
    

        

#Model to store tyre information concerning every vehicle
class Tyre(models.Model):
    Tyre_code = models.CharField(max_length = 45,primary_key=True, db_column='Tyre_code', unique=True)
    Plate_Number = models.OneToOneField(Vehicle,max_length=20, db_column='Plate_Number',null=True, on_delete=models.CASCADE)
    Tyre_model = models.CharField(max_length=45, db_column='Tyre_model')
    Tyre_brand = models.CharField(max_length=45, db_column='Trye_brand')
    Tyre_size = models.CharField(max_length=20,db_column='Tyre_size')
    Tread_depth = models.IntegerField(db_column='Tread_depth')
    Tyre_description = models.TextField(max_length=500, db_column='Tyre_description')
    Load_capacity = models.CharField(max_length = 20,db_column='Load_capacity')
    Material = models.CharField(max_length=20, db_column='Material')
    Rim_width = models.CharField(max_length= 20,db_column='Rim_width')
    Section_width = models.CharField(max_length=20, db_column='Section_width')
    Radius = models.CharField(max_length=20, db_column='Radius')
    Speed_rating = models.CharField(max_length=20, db_column='Speed_rating')
    Wear_and_tear = models.CharField(max_length=30, db_column='Wear_and_tear')
    Tyre_service_mileage = models.CharField(max_length=20, db_column='Tyre_service_mileage')


    class Meta:
        db_table = 'TYRE'
        ordering = ('Tyre_code',)

    def __str__(self):
        return self.Tyre_model and self.Tyre_brand

#Fault model to store the particular faults that are entered by either the driver of a particular vehicle   
class Fault(models.Model):
    Fault_id = models.AutoField(primary_key=True, db_column='Fault_id', unique=True)
    Description = models.CharField(max_length=45, db_column='Description')
    Date_of_Occurence = models.DateTimeField(db_column='Date_of_Occurence', default=0)
    Fault_Status = models.CharField(max_length=45, db_column='Fault_Status')
    #Vehicle_id = models.ForeignKey(Vehicle, models.DO_NOTHING, db_column='Vehicle_id', blank=True, null=True)
    Plate_Number = models.ForeignKey(Vehicle, models.DO_NOTHING, db_column='Plate_Number', blank=True, null=True)
    PersonID = models.ForeignKey(Person, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)
    
    class Meta:
        db_table = 'FAULT'
        ordering = ('Fault_id',)
    
    def __str__(self):
        return self.Description
    
#Service Schedule model to store the different service schedules
class Service_schedule(models.Model):
    Schedule_id = models.AutoField(primary_key=True, db_column='Schedule_id', unique=True)
    Year = models.DateField(db_column='Year')
    Service_Mileage = models.IntegerField(db_column='Service_Mileage')
    Service_Items =models.CharField(max_length=45, db_column='Service_Items')
    Level_code = models.CharField(max_length=5, db_column='Level_code')
    #Vehicle_id = models.ForeignKey(Vehicle, models.DO_NOTHING, db_column='Vehicle_id', blank=True, null=True)
    Plate_Number = models.ForeignKey(Vehicle, models.DO_NOTHING, db_column='Plate_Number', blank=True, null=True)
    #PersonID = models.ForeignKey(Staff, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)
    
    class Meta:
        db_table = 'SERVICE_SCHEDULE'
        ordering = ('Schedule_id',)
    
    def __str__(self):
        return self.Schedule_id

#Maintenance type model to store the different maintenance types for the respective faults
class Maintenance_type(models.Model):
    Maintenance_Type_ID = models.AutoField(primary_key=True, db_column='Maintenance_Type_ID', unique=True)
    Fault_id = models.ForeignKey(Fault, models.DO_NOTHING, db_column='Fault_id', blank=True, null=True)
    Schedule_id = models.ForeignKey(Service_schedule, models.DO_NOTHING, db_column='Schedule_id', blank=True, null=True)
    Description = models.CharField(max_length=30, db_column='Description')
    
    class Meta:
        db_table = 'MAINTENANCE_TYPE'
        ordering = ('Maintenance_Type_ID',)
    
    def __str__(self):
        return self.Description 


    
    

#Work Order model to store the different workorders both pending, approved and completed
class Work_order(models.Model):
    WORK_ORDER_id = models.AutoField(primary_key=True, db_column='WORK_ORDER_id', unique=True)
    Date_of_Creation = models.DateField(db_column='Date_of_Creation')
    Date_of_Approval = models.DateField(db_column='Date_of_Approval')
    Estimated_Cost = models.CharField(max_length=45, db_column='Estimated_Cost')
    Date_of_Completion= models.DateField(db_column='Date_of_Completed')
    Garage_Name = models.OneToOneField(Garage, models.DO_NOTHING, db_column='GarageName', blank=True, null=True) 
    PersonID = models.ForeignKey(Person, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)  
    MAINTENANCE_TYPE_id = models.ForeignKey(Maintenance_type, models.DO_NOTHING, db_column='MAINTENANCE_TYPE_id', blank=True, null=True)  
    
    class Meta:
        db_table = 'WORK_ORDER'
        ordering = ('Date_of_Creation',)
    
    def __str__(self):
        return self.WORK_ORDER_id
    

#Model for the Maintenance record to store the different maintenance records for the respective faults and service schedules per vehicle
class Maintenance_record(models.Model):
    Maintenance_record_id = models.AutoField(primary_key=True, db_column='Maintenance_record_id', unique=True)
    Start_date = models.DateTimeField(db_column='Start_date')
    Completion_date = models.DateTimeField(db_column='Completion_date')
    Description_of_Maintenance_actions = models.CharField(max_length=200, db_column='Description_of_Maintenance_actions')
    Maintenance_cost = models.CharField(max_length=20, db_column='Maintenance_cost')

    #defining the status choices
    STATUS_CHOICES = (
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    )
    Maintenance_Status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Ongoing', db_column='Maintenance_Status')
    Maintenance_type_ID = models.ForeignKey(Maintenance_type, models.DO_NOTHING, db_column='Maintenance_Type_ID', null=False)
    WORK_ORDER_id = models.ForeignKey(Work_order, models.DO_NOTHING, db_column='WORK_ORDER_id', null=False)
    PersonID = models.ForeignKey(Person, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)
    Plate_Number = models.ForeignKey(Vehicle, models.DO_NOTHING, db_column='Plate_Number', blank=False, null=False)

    class Meta:
        db_table = 'MAINTENANCE_RECORD'
        ordering = ('Maintenance_record_id',)