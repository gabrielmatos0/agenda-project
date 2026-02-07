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
    # class Meta:
    #     model = Contact
    #     fields = (
    #         'first_name', 'last_name', 'phone', 'email', 'description', 'category',
    #     )
    #     widgets = {
    #         'first_name': forms.TextInput(
    #             attrs={
    #                 'class': 'class-a class-b',
    #                 'placeholder': 'type your first name right here',
    #             },
    #         )
    #     }

    #     help_texts = {
    #         'first_name': 'texto de ajuda pro usuário'
    #     }

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

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',
        )
    ### in all 3 cases I will need to set fields and model attributes in the Meta class 
    # class Meta:
    #     model = MyModel
    #     fields = (
    #         'field1', 'fiedl2', 'fiedl3',
    #     )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error('first_name', ValidationError("First name can't be equal to last name", code='invalid'))
            self.add_error('last_name', ValidationError("First name can't be equal to last name", code='invalid'))

        print(self.cleaned_data)
        print(self.cleaned_data.get('first_name'))

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite ABC neste campo',
                    code='invalid'
                )
            )

        return first_name
