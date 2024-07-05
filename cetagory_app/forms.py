from django import forms

from cetagory_app.models import add_cetagory

class cetagory_form(forms.ModelForm):
    class Meta:
        model =  add_cetagory
        fields = "__all__"