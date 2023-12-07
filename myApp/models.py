from django.db import models

class Student_M(models.Model):
    Student_Name = models.CharField(max_length=50)
    Student_Class = models.CharField(max_length=50)
    Student_Roll = models.CharField(max_length=50)
    Student_Bgroup = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Student_Class+" "+ self.Student_Name

class Teacher_M(models.Model):
    Teacher_Name = models.CharField(max_length=50)
    Teacher_Department = models.CharField(max_length=50)
    Teacher_Resignation = models.CharField(max_length=50)
    Teacher_Bgroup = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Teacher_Name+ " " + self.Teacher_Department