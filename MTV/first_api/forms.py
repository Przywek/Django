from django import forms
from first_api.models import Users
class User_form(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
