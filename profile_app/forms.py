from django import forms
from profile_app.models import profile

class profile_form(forms.ModelForm):
    class Meta:
        model = profile
        fields = '__all__'