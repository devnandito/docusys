from django import forms
from docusys.clients.models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'ci', 'email', 'phone', 'direction', 'birthday',)