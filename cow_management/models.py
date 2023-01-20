from django.db import models

# Create your models here.
kinds_male=[("nnume","nnume"), ("ndaawo","ndaawo"),("kalume","kalume")]
kinds_female=[("mugongo","mugongo"), ("nduusi","nduusi"),("kaluusi","kaluusi")]
breeds=[("local","local breed"), ("cross","cross breed")]
   
class Male(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    mother = models.ForeignKey("Female", on_delete=models.SET_NULL, null=True, default=None)
    father = models.ForeignKey("Male", on_delete=models.SET_NULL, null=True, default=None)
    dob = models.DateField(auto_now=True)
    category= models.CharField(max_length=10, choices=kinds_male)
    type= models.CharField(max_length=255, choices=breeds)

class Female(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    mother = models.ForeignKey("Female", on_delete=models.SET_NULL, null=True, default=None)
    father = models.ForeignKey("Male", on_delete=models.SET_NULL, null=True, default=None)
    isPregnant = models.BooleanField(default=False)
    dob = models.DateField(auto_now=False, null=True)
    estDob = models.DateField(auto_now=False)
    category= models.CharField(max_length=10, choices=kinds_female)
    type= models.CharField(max_length=255, choices=breeds)
    
    def est_dob(self,estDob):
        pass