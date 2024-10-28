from django.db import models
from django.contrib import admin
class bankloan(models.Model):
	Name=models.CharField(max_length=10)
	Accountno=models.IntegerField(primary_key="Accountno")
	Interest=models.FloatField()
	Startdate=models.DateField()
	Email=models.EmailField()
	Mobilenumber=models.IntegerField()
	Amount=models.IntegerField()
	Enddate=models.DateField()

class bankloanAdmin(admin.ModelAdmin):
	list_display=('Name','Accountno','Interest','Startdate','Email','Mobilenumber','Amount','Enddate')