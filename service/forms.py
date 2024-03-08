from django import forms
from models import register_form

class Registration(forms.ModelsForms):
    class Meta:
        model = register_form
        fields = {'firstname','lastname','phone_no','password'}