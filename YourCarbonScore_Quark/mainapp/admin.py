from django.contrib import admin
from .models import Oxygen_Emission, Vehicle_CO2_Emission, HomeAppliance_CO2_Emission, Waste_Management, Carbon_Score

# Register your models here.
admin.site.register(Oxygen_Emission)
admin.site.register(Vehicle_CO2_Emission)
admin.site.register(HomeAppliance_CO2_Emission)
admin.site.register(Waste_Management)
admin.site.register(Carbon_Score)