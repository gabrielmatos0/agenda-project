from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):

    ### I can set a field input like this
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # self.model = Contact
    #     self.fields['first_name'].widget.attrs.update({
    #         'class': 'class-c class-d',
    #         'placeholder': 'type your primeiro nome right here'
    #     })

    ### or like this
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class-e class-f',
                'placeholder': 'type your first nome right here'
            }
        ),
        help_text='help text to the user'
    )
    any = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class-y class-z',
                'placeholder': 'type anything here'
            }
        ),
        help_text='help text to the user'
    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
        ### or like this
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'class-a class-b',
        #             'placeholder': 'type your first name right here',
        #         },
        #     )
        # }

        # help_texts = {
        #     'first_name': 'texto de ajuda pro usuário'
        # }
    ### in all 3 cases I will need to set fields and model attributes in the Meta class 
    # class Meta:
    #     model = MyModel
    #     fields = (
    #         'field1', 'fiedl2', 'fiedl3',
    #     )

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(None, ValidationError('falta esse campo aqui meu patrão', code='invalid'))

        self.add_error(None, ValidationError('errastes de novo.', code='invalid'))

        return super().clean()
