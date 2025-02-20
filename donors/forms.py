from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"
        widgets = {
            "last_donation": forms.DateInput(attrs={"type": "date"})
        }
