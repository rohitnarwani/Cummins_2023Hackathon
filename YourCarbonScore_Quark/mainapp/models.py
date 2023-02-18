from django.db import models
from userauth.models import Account
from django.utils import timezone

# Create your models here.
class Oxygen_Emission(models.Model):
    plant_species = models.CharField(max_length=30)
    light_intensity = models.DecimalField(max_digits=5, decimal_places=2)
    carbon_emission = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)

    submitted_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    oxygen_emission = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.user.fullname + self.submitted_on.strftime(f" - [%d %B %Y]")

class Vehicle_CO2_Emission(models.Model):
    engine_type = models.CharField(max_length=30) # Inline 4, V6, V8
    cylinders = models.IntegerField()
    transmission = models.CharField(max_length=30) # Automatic, CVT, Manual
    fuel_type = models.CharField(max_length=30) # Diesel, Electric, Hybrid, Petrol
    
    submitted_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    CO2_emissions = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.user.fullname + self.submitted_on.strftime(f" - [%d %B %Y]")

class HomeAppliance_CO2_Emission(models.Model):
    appliance_type = models.CharField(max_length=30)
    electricity_units = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.DecimalField(max_digits=5, decimal_places=2)
    maintenance = models.CharField(max_length=30) # Regular, Irregular
    submitted_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    CO2_emissions = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.user.fullname + self.submitted_on.strftime(f" - [%d %B %Y]")

class Waste_Management(models.Model):
    e_waste = models.DecimalField(max_digits=5, decimal_places=2)
    proper_disposal = models.DecimalField(max_digits=5, decimal_places=2) # in %
    composting = models.DecimalField(max_digits=5, decimal_places=2) # in %
    recycling = models.DecimalField(max_digits=5, decimal_places=2) # in %
    
    submitted_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    CO2_emissions = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.user.fullname + self.submitted_on.strftime(f" - [%d %B %Y]")
    

class Carbon_Score(models.Model):
    carbon_score    = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    submitted_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.fullname + self.submitted_on.strftime(f" - [%d %B %Y]")