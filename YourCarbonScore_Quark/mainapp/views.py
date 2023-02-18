from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.decorator import login_required_message
from .models import Oxygen_Emission, HomeAppliance_CO2_Emission, Vehicle_CO2_Emission, Waste_Management, Carbon_Score
from userauth.models import Account
from utils.ml_helpers import predictOxygenEmission, predictHomeApplianceCarbonDioxide, predictVehicleCarbonDioxide, predictWasteManagementCO2Emission
from utils.score_generator import get_carbon_score
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('adminuser')

        carbon_scores = []
        dates = []
        if len(Carbon_Score.objects.filter(user=request.user)) > 0:
            carbon_score_obj = Carbon_Score.objects.filter(user=request.user)
            line_carbon_score_array = carbon_score_obj.order_by('submitted_on')

            for score in line_carbon_score_array.values('carbon_score', 'submitted_on'):
                carbon_scores.append(float(score['carbon_score']))
                dates.append(score['submitted_on'].strftime("%d %B %Y"))
            carbon_score_single = carbon_score_obj.order_by('-submitted_on')[0]
            carbon_score = carbon_score_single.carbon_score
        else:
            carbon_score = False

        if len(HomeAppliance_CO2_Emission.objects.filter(user=request.user)) > 0:
            home_appliance_co2_val = HomeAppliance_CO2_Emission.objects.filter(user=request.user).order_by('-submitted_on')[0].CO2_emissions
            home_appliance_co2_val = float(home_appliance_co2_val)
        else:
            home_appliance_co2_val = False
        if len(Vehicle_CO2_Emission.objects.filter(user=request.user)) > 0:
            vehicle_co2_val = Vehicle_CO2_Emission.objects.filter(user=request.user).order_by('-submitted_on')[0].CO2_emissions
            vehicle_co2_val = float(vehicle_co2_val)
        else:
            vehicle_co2_val = False
        if len(Waste_Management.objects.filter(user=request.user)) > 0:
            waste_management_co2_val = Waste_Management.objects.filter(user=request.user).order_by('-submitted_on')[0].CO2_emissions
            waste_management_co2_val = float(waste_management_co2_val)
        else:
            waste_management_co2_val = False
        
        carbon_score_array = [home_appliance_co2_val, vehicle_co2_val, waste_management_co2_val]

        if len(carbon_scores) > 0:
            show_line_chart = True
        else:
            show_line_chart = False
        
        if carbon_score_array[0] != False or carbon_score_array[1] != False or carbon_score_array[2] != False:
            if carbon_score_array[0] == False:
                carbon_score_array[0] = 0
            if carbon_score_array[1] == False:
                carbon_score_array[1] = 0
            if carbon_score_array[2] == False:
                carbon_score_array[2] = 0
            show_pie_chart = True
        else:
            show_pie_chart = False


        context = {
            'show_line_chart': show_line_chart,
            'show_pie_chart': show_pie_chart,
            'carbon_scores': carbon_scores,
            'dates': dates,
            'carbon_score_array': carbon_score_array,
            'carbon_score': round(carbon_score, 3),
            'carbon_score_scroll': request.GET.get('carbon_score_scroll')
        }
        return render(request, 'mainapp/home.html', context)
    return render(request, 'mainapp/index.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def oxygen_emission(request):
    if request.user.is_admin:
            return redirect('adminuser')
    if request.method == "POST":
        data = request.POST

        plant_species = data['plant_species']
        plant_species = plant_species.strip().title()
        light_intensity = data['light_intensity']
        carbon_emission = data['carbon_emission']
        temperature = data['temperature']
        
        try:
            ans = predictOxygenEmission(plant_species=plant_species, light_intensity=light_intensity, carbon_emission=carbon_emission, temperature=temperature)
            oxygen_model = Oxygen_Emission(plant_species=plant_species, light_intensity=light_intensity, carbon_emission=carbon_emission, temperature=temperature, user=request.user, oxygen_emission=ans)
            oxygen_model.save()

            # if len(Carbon_Score.objects.filter(user=request.user)):
            #     oxygen_val = Oxygen_Emission.objects.filter(user=request.user).order_by('-submitted_on')[0].oxygen_emission
            # else:
            #     oxygen_val = 0
            
            if len(HomeAppliance_CO2_Emission.objects.filter(user=request.user)):
                home_appliance_co2_val = HomeAppliance_CO2_Emission.objects.filter(user=request.user).order_by('-submitted_on')[0].CO2_emissions
            else:
                home_appliance_co2_val = 0
            
            if len(Vehicle_CO2_Emission.objects.filter(user=request.user)) > 0:
                vehicle_co2_val = Vehicle_CO2_Emission.objects.filter(user=request.user).order_by('-submitted_on')[0].CO2_emissions
            else:
                vehicle_co2_val = 0
            
            if len(Waste_Management.objects.filter(user=request.user)) > 0:
                waste_management_co2_val = Waste_Management.objects.filter(user=request.user).order_by('-submitted_on')[0].CO2_emissions
            else:
                waste_management_co2_val = 0
            user = request.user

            get_carbon_score(ans, home_appliance_co2_val, vehicle_co2_val, waste_management_co2_val, user)
            
            context = {
                'ans': round(ans, 3),
                'has_ans': True,
            }
            return render(request, 'mainapp/oxygen_emission.html', context)
        except ValueError:
            messages.error(request, 'Please enter a valid input.')

        context = {}    
        return render(request, 'mainapp/oxygen_emission.html', context)
        
        

        
    return render(request, 'mainapp/oxygen_emission.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def homeappliances(request):
    if request.user.is_admin:
            return redirect('adminuser')
    if request.method == "POST":
        data = request.POST
        appliance_type = data['appliance_type']
        appliance_type = appliance_type.strip().title()
        electricity_units = data['electricity_units']
        age = data['age']
        maintenance = data['maintenance']

        try:
            ans = predictHomeApplianceCarbonDioxide(electricity_units, age, maintenance, appliance_type)
            appliance_model = HomeAppliance_CO2_Emission(appliance_type=appliance_type, electricity_units=electricity_units, age=age, maintenance=maintenance, user=request.user, CO2_emissions=ans)
            appliance_model.save()
            context = {
            'ans': round(ans, 3),
            'has_ans': True,
            }
            return render(request, 'mainapp/homeappliances.html', context)
            
        except ValueError:
            messages.error(request, 'Please enter a valid input.')
        
        context = {}
        return render(request, 'mainapp/homeappliances.html', context)
    return render(request, 'mainapp/homeappliances.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def vehicles(request):
    if request.user.is_admin:
            return redirect('adminuser')
    if request.method == 'POST':
        data = request.POST
        engine_type = data['engine_type']
        cylinders = data['cylinders']
        transmission = data['transmission']
        fuel_type = data['fuel_type']

        ans = predictVehicleCarbonDioxide(engine_type, cylinders, transmission, fuel_type)

        vehicle_model = Vehicle_CO2_Emission(engine_type=engine_type, cylinders=cylinders, transmission=transmission, fuel_type=fuel_type, user=request.user, CO2_emissions=ans)
        vehicle_model.save()
     
        context = {
            'ans': round(ans, 3),
            'has_ans': True,
        }
        return render(request, 'mainapp/vehicles.html', context)

    return render(request, 'mainapp/vehicles.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def waste(request):
    if request.user.is_admin:
            return redirect('adminuser')
    if request.method == 'POST':
        data = request.POST

        e_waste = data['e_waste']
        proper_disposal = data['proper_disposal']
        composting = data['composting']
        recycling = data['recycling']

        ans = predictWasteManagementCO2Emission(e_waste, proper_disposal, composting, recycling)

        waste_model = Waste_Management(e_waste=e_waste, proper_disposal=proper_disposal, composting=composting, recycling=recycling, user=request.user, CO2_emissions=ans)
        waste_model.save()

        context = {
            'ans': round(ans, 3),
            'has_ans': True,
        }
        return render(request, 'mainapp/waste.html', context)
    return render(request, 'mainapp/waste.html')

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def leaderboard(request):
    if request.user.is_admin:
        return redirect('adminuser')
    users = Account.objects.filter(is_admin=False).values('fullname', 'id')
    users = list(users)
    max_carbon_score = 10000
    for user in users:
        if len(Carbon_Score.objects.filter(user=user['id'])) > 0:
            carbon_score_obj = Carbon_Score.objects.filter(user=user['id']).order_by('-submitted_on')[0]
            carbon_score = float(carbon_score_obj.carbon_score)
            user['show'] = True
            user['carbon_score'] = carbon_score
        else:
            user['show'] = False
            user['carbon_score'] = max_carbon_score

    users = sorted(users, key=lambda x: x['carbon_score'])

    context = {
        'users':users,
    }
    return render(request, 'mainapp/leaderboard.html', context)