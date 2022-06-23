from django.db import models

# Create your models here.

class Management (models.Model):
    Room_Number = models.IntegerField()
    Amount_Paid = models.CharField(max_length=100)
    Occupant_First_Name = models.CharField(max_length=100)
    Occupant_Last_Name = models.CharField(max_length=100)
    Occupant_Email = models.EmailField(max_length=100)
    Occupant_Occupation = models.CharField(max_length=150)
    Number_Of_Nights = models.IntegerField()
    Start_Date = models.DateTimeField()
    End_Date = models.DateTimeField()
    
    def __str__(self):
        return self.Room_Number