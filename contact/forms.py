from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(None, ValidationError('falta esse campo aqui meu patrão', code='invalid'))

        self.add_error(None, ValidationError('errastes de novo.', code='invalid'))

        return super().clean()
