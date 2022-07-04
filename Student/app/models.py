from pickle import TRUE
from django.db.models.signals  import post_save
from django.dispatch import receiver
from ast import Mod
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile_number=models.CharField(max_length=199)
    gender=models.CharField(max_length=10,choices=(('Male','male'),('Female','female'),('Other','other')))
    course=models.CharField(max_length=10,choices=(('BCA','BCA'),('BBA','BBA'),('B.Tech','B.Tech'),('MBA','MBA'),('MCA','MCA'),('M.Tech','M.Tech')))
    current_address=models.TextField(max_length=300)
    marks_te=models.IntegerField(default=False)
    percentage_te=models.FloatField(default=False)
    passing_year_te=models.IntegerField(default=False)
    marks_tw=models.IntegerField(default=False)
    percentage_tw=models.FloatField(default=False)
    passing_year_tw=models.IntegerField(default=False)
    marks_ug=models.IntegerField(default=False)
    percentage_ug=models.FloatField(default=False)
    passing_year_ug=models.IntegerField(default=False)
    marks_m=models.IntegerField(default=False)
    percentage_m=models.FloatField(default=False)
    passing_year_m=models.IntegerField(default=False)
    marksheet_te=models.FileField(upload_to="document/10")
    marksheet_tw=models.FileField(upload_to="document/12")
    marksheet_ug=models.FileField(upload_to="document/UG")
    marksheet_m=models.FileField(upload_to="document/PG")
    def __str__(self):
        return str(self.user.username)

@receiver(post_save, sender=User)
def update_customer_settings(sender, instance, created, **kwargs):
    
        if created:
            pd=Student()
            pd.user=instance
            pd.save()

    