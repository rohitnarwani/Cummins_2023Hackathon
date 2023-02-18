from wocv.models import OfficeHours
from django import forms

class Officehours(forms.ModelForm):
    class Meta():
        model=OfficeHours
        fields=("starttime",
    "endtime")