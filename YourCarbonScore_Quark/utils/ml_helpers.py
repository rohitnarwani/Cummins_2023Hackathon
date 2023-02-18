import pickle
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=FutureWarning)

# Predict function for oxygen emission prediction

def predictOxygenEmission(plant_species,light_intensity, carbon_emission, temperature):
    with open('utils/Pickle_Files/label.pickle', 'rb') as handle:
        b = pickle.load(handle)
    model=pickle.load(open('utils/Pickle_Files/model.pkl', 'rb'))
    val=b.get(plant_species)
    ans=model.predict([[val,light_intensity, carbon_emission, temperature]])
    return ans[0]

# Predict function for Home Appliance carbon dioxide emission

def predictHomeApplianceCarbonDioxide(electricity, age, maintenance, appliance_type):
    with open('utils/Pickle_Files/maintenance.pickle', 'rb') as handle:
        b1 = pickle.load(handle)
    with open('utils/Pickle_Files/appliance_type.pickle', 'rb') as handle:
        b2 = pickle.load(handle)
    model=pickle.load(open('utils/Pickle_Files/home_appliances_co2.pkl', 'rb'))
    val1=b1.get(maintenance)
    val2=b2.get(appliance_type)
#     val3=b3.get(fuel_type)
    ans=model.predict([[electricity, age, val1, val2]])
    return ans[0]

# Predict function for vehicle carbon emission 

def predictVehicleCarbonDioxide(engine_type, cylinders, transmission, fuel_type):
    with open('utils/Pickle_Files/engine_type.pickle', 'rb') as handle:
        b1 = pickle.load(handle)
    with open('utils/Pickle_Files/transmission.pickle', 'rb') as handle:
        b2 = pickle.load(handle)
    with open('utils/Pickle_Files/fuel_type.pickle', 'rb') as handle:
        b3 = pickle.load(handle)
    model=pickle.load(open('utils/Pickle_Files/vehicle_co2.pkl', 'rb'))
    val1=b1.get(engine_type)
    val2=b2.get(transmission)
    val3=b3.get(fuel_type)
    ans=model.predict([[val1,cylinders, val2, val3]])
    return ans[0]

# Waste management CO2 emission predict function

def predictWasteManagementCO2Emission(e_waste, proper_disposal, composting, recycling):
    model=pickle.load(open('utils/Pickle_Files/waste_management_model.pkl', 'rb'))
    ans=model.predict([[e_waste, proper_disposal, composting, recycling]])
    return ans[0]