from django import forms  
from .models import *  
class CaraccidentForm(forms.ModelForm):  
    class Meta:  
        model = Caraccident
        fields = "__all__"  