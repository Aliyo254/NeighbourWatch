from .models import Neighbourhood,Profile,Business,Post
from django import forms

class NewNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        exclude=['admin']
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_pic','bio']