from django import forms

from author_app.models import add_author

class author_form(forms.ModelForm):
    class Meta:
        model = add_author
        fields = "__all__"