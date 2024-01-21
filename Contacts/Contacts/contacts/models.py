from django.db import models

# Create your models here.


class Staff(models.Model):
    Name = models.CharField(max_length=30)
    Phone_no = models.CharField(max_length=10)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.Name}"
    
       


class Position(models.Model):
    Designation = models.CharField(max_length=50)
    Direct_Report = models.CharField(max_length=50)
    Superior = models.CharField(max_length=50)
    Location = models.ForeignKey("Address", related_name = 'Posted_to_Address', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Designation}"
    
    
    
    

class Posted(models.Model):
    Date = models.DateField()
    Designation = models.ForeignKey("Position", related_name = 'Posted_to_Designation', on_delete=models.CASCADE)
    Name = models.ForeignKey("Staff", related_name = 'Posted_to_Name', on_delete=models.CASCADE)
    Location = models.ForeignKey("Position", related_name = 'Posted_to_Location', on_delete=models.CASCADE)

    
    

class MnEStaff(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=10)

    def __str__(self):
        return self.Name

class Engagement(models.Model):
    Engagement_Name = models.CharField(max_length=50)
    Engagement_Type = models.CharField(max_length=50)
    Description = models.TextField()
    Department = models.ForeignKey("Address", related_name = '+', on_delete=models.CASCADE)

    def __str__(self):
        return self.Engagement_Name
    

class Address(models.Model):
    Department = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    Physical_Address = models.CharField(max_length=50)

    def __str__(self):
        return self.Company

class Activities(models.Model):
    Date_completed = models.DateField()
    Due_Date = models.DateField()
    Name = models.ForeignKey("MnEStaff", related_name = 'Posted_to_Name', on_delete=models.CASCADE)
    Engagement_Name = models.ForeignKey("Engagement", related_name = "+", on_delete=models.CASCADE)
    Department = models.ForeignKey("Address", related_name ='Posted_to_Department', on_delete=models.CASCADE)

