from django import forms    
from .models import Pro

class ProductForm(forms.ModelForm): 
    class Meta: 
        model = Pro
        fields = [
            'title',
            'description',
            'price',
        ]