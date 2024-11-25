from django.forms import ModelForm
from .models import table

class tableform(ModelForm):
    class Meta:
        model = table
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']