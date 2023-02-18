from mainapp.models import Carbon_Score
from dotenv import load_dotenv
from utils.email_sender import send_mail
import os

def get_carbon_score(oxygen_val, home_appliance_co2_val, vehicle_co2_val, waste_management_co2_val, user):
        mean_co2_emission = (home_appliance_co2_val+vehicle_co2_val+waste_management_co2_val)/3
        
        net_carbon_emission = float(mean_co2_emission) - float(oxygen_val)
        
        carbon_score_model = Carbon_Score(carbon_score=net_carbon_emission, user=user)

        load_dotenv()
        if net_carbon_emission < 0:
                send_mail(user.email, f"Check your Carbon score.", f"Hey {user.fullname}. Congratulations!! Your carbon score is net-negative ({net_carbon_emission}). Check it out here {os.getenv('WEB_URL')}#carbon_score")
        else:
                send_mail(user.email, f"Check your Carbon score.", f"Hey {user.fullname}. You need to work on reducing your carbon footprint. Your carbon score is net-positive ({net_carbon_emission}). Check it out here {os.getenv('WEB_URL')}#carbon_score")


        carbon_score_model.save()