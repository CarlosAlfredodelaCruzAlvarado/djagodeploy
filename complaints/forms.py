from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            'title', 'description', 'product_service', 'category', 
            'manufacturer', 'problem_date', 'location', 'frequency', 
            'impact', 'evidence', 'anonymous', 'contact_email'
        ]
