from django.db import models

from django.contrib.auth.models import AbstractUser

#Customizing the User model
class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username

#This is the Access Level model
class Access_level(models.Model):
    Access_Level_ID = models.IntegerField(primary_key=True, null=False, db_column='Access_Level_id')
    Description = models.CharField(max_length=50, db_column='Description')
    
    class Meta:
        db_table = 'ACCESS_LEVEL'
        ordering = ('Access_Level_ID',)
    
    def __str__(self):
        return self.Description
    
    
#This is an abstract model to be inherited by the Garage manager and the staff models
class Person(models.Model):
    PersonID = models.AutoField(primary_key=True, db_column='Person_id', unique=True)
    FName = models.CharField(max_length=20,db_column='FName')
    LName = models.CharField(max_length=20,db_column='LName')
    UserName = models.CharField(max_length=20,db_column='UserName')
    Password = models.CharField(max_length=20, db_column='Password')
    Address = models.CharField(max_length=45, db_column='Address')
    email = models.CharField(max_length=45, db_column='Email')
    PhoneNo = models.IntegerField(default=0, db_column='PhoneNo')
    Access_Level_ID = models.OneToOneField(Access_level, models.DO_NOTHING, db_column='Access_Level_ID', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        db_table = 'PERSON'
        ordering = ('PersonID',)
        abstract = True
        
    def __str__(self):
        return self.FName and self.LName
    

#This is the Garage_manager model that inherits atributes from the Person Model   
class Garage_manager(Person):
    
    class Meta(Person.Meta):
        db_table = 'GARAGE_MANAGER'
        ordering = ('PersonID',)
    
    def __str__(self):
        return self.FName and self.LName
    
        
#This is the Garage model that creates table to store information about the Garages
class Garage(models.Model):
    GarageID = models.AutoField(primary_key=True)
    GarageName = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    WorkOrderNo = models.IntegerField(default=0)
    PersonID = models.ForeignKey(Garage_manager, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        db_table = 'GARAGE'
        ordering = ('GarageID',)
    
    def __str__(self):
        return self.GarageName

#Staff model inherits the person model but specialises on the specific internal staff
class Staff(Person):
    Responsibility = models.CharField(max_length=50)
    class Meta(Person.Meta):
        db_table = 'STAFF'
        ordering = ('PersonID',)
        verbose_name_plural ='Staff'
    
    def __str__(self):
        return self.FName and self.LName

#Vehilce_type model to store the vehilce types and descriptions
class Vehicle_type(models.Model):
    Vehicle_Type_ID = models.IntegerField(primary_key=True, db_column='Vehicle_Type_ID', unique=True)
    Description = models.CharField(max_length=30, db_column='Description')
    
    class Meta:
        db_table = 'VEHICLE_TYPE'
        ordering = ('Vehicle_Type_ID',)
    
    def __str__(self):
        return self.Description

#Vehicle model to store information on particular vehicles 
class Vehicle(models.Model):
    Vehicle_id = models.IntegerField(primary_key=True, db_column='Vehicle_id', unique=True)
    VIN = models.CharField(max_length=45, db_column='VIN')
    Plate_No = models.CharField(max_length=20, db_column='Plate_No')
    Make = models.CharField(max_length=30, db_column='Make')
    Model= models.CharField(max_length=30, db_column='Model')
    Year = models.DateField(db_column='Year')
    Colour = models.CharField(max_length=20, db_column='Colour')	
    Put_in_service_Date = models.DateTimeField(db_column='Put_in_service_Date')
    Taken_out_of_service_Date = models.DateTimeField(db_column='Taken_out_of_service_Date')
    Mileage = models.IntegerField(db_column='Mileage')
    Tire_Size = models.IntegerField(db_column='Tire_Size')
    Down_Time = models.CharField(max_length = 20, db_column='Down_Time')
    Service_Interval = models.IntegerField(db_column='Service_Interval')
    PersonID = models.ForeignKey(Staff, related_name='PERSON_PERSON_id', on_delete=models.CASCADE, db_column='PersonID', blank=True, null=True)  
    VEHICLE_TYPE_id = models.ForeignKey(Vehicle_type, models.DO_NOTHING, db_column='VEHICLE_TYPE_id', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        ordering = ['Put_in_service_Date', 'Taken_out_of_service_Date']
        db_table = 'VEHICLE'
    
    def __str__(self):
        return self.VIN and self.Plate_No
    

        return self.Description

#Fault model to store the particular faults that are entered by either the driver of a particular vehicle   
class Fault(models.Model):
    Fault_id = models.IntegerField(primary_key=True, db_column='Fault_id', unique=True)
    Description = models.CharField(max_length=45, db_column='Description')
    Date_of_Occurence = models.DateTimeField(db_column='Date_of_Occurence', default=0)
    Fault_Status = models.CharField(max_length=45, db_column='Fault_Status')
    Vehicle_id = models.ForeignKey(Vehicle, models.DO_NOTHING, db_column='Vehicle_id', blank=True, null=True)
    PersonID = models.ForeignKey(Staff, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)
    
    class Meta:
        db_table = 'FAULT'
        ordering = ('Fault_id',)
    
    def __str__(self):
        return self.Description
    
#Service Schedule model to store the different service schedules
class Service_schedule(models.Model):
    Schedule_id = models.IntegerField(primary_key=True, db_column='Schedule_id', unique=True)
    Year = models.DateField(db_column='Year')
    Service_Mileage = models.IntegerField(db_column='Service_Mileage')
    Service_Items =models.CharField(max_length=45, db_column='Service_Items')
    Level_code = models.CharField(max_length=5, db_column='Level_code')
    Vehicle_id = models.ForeignKey(Vehicle, models.DO_NOTHING, db_column='Vehicle_id', blank=True, null=True)
    PersonID = models.ForeignKey(Staff, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)
    
    class Meta:
        db_table = 'SERVICE_SCHEDULE'
        ordering = ('Schedule_id',)
    
    def __str__(self):
        return self.Schedule_id

#Maintenance type model to store the different maintenance types for the respective faults
class Maintenance_type(models.Model):
    Maintenance_Type_ID = models.IntegerField(primary_key=True, db_column='Maintenance_Type_ID', unique=True)
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
    WORK_ORDER_id = models.IntegerField(primary_key=True, db_column='WORK_ORDER_id', unique=True)
    Date_of_Creation = models.DateField(db_column='Date_of_Creation')
    Date_of_Approval = models.DateField(db_column='Date_of_Approval')
    Estimated_Cost = models.CharField(max_length=45, db_column='Estimated_Cost')
    Date_of_Completed = models.DateField(db_column='Date_of_Completed')
    GarageName = models.OneToOneField(Garage, models.DO_NOTHING, db_column='GarageName', blank=True, null=True) 
    PersonID = models.ForeignKey(Staff, models.DO_NOTHING, db_column='PersonID', blank=True, null=True)  
    MAINTENANCE_TYPE_id = models.ForeignKey(Maintenance_type, models.DO_NOTHING, db_column='MAINTENANCE_TYPE_id', blank=True, null=True)  
    
    class Meta:
        db_table = 'WORK_ORDER'
        ordering = ('Date_of_Creation',)
    
    def __str__(self):
        return self.WORK_ORDER_id