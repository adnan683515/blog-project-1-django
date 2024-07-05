from django import forms

from post_app.models import add_post

class post_form(forms.ModelForm):
    class Meta:
        model =  add_post
        fields = "__all__"