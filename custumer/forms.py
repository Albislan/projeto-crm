from django import forms
from django.forms.widgets import DateInput
from .models import Custumer

class DateInput(forms.DateInput):
    input_type = "date"

class CustumerForm(forms.ModelForm):
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    email = forms.EmailField(label="e-mail")
    birth_date = forms.DateField(label="data de nascimento", widget=DateInput())
    area_code = forms.RegexField(label="DDD", regex=r"^\+?1?[0-9]{2}$", error_messages={"ivalid": "Número de DDD inválido"})
    phone_number = forms.RegexField(label="número de telefone", regex=r"^\+?1?[0-9]{9,15}$", error_messages={"ivalid": "Número de Telefone Inválido"})
    country = forms.CharField(label="país")
    state = forms.CharField(label="estado")
    city = forms.CharField(label="cidade")

    class Meta:
        model = Custumer
        fields = {
             "first_name",
             "last_name", 
             "email",
             "birth_date",
             "area_code",
             "phone_number",
             "country",
             "state",
             "city",
        }