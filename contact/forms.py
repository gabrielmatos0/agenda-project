from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu primeiro nome',
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu sobrenome',
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Digite seu E-mail',
            },
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Este email já está cadastrado',
                    code='invalid'
                )
            )

        return email


class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)

    email = forms.EmailField(
        required=True,
        help_text='Digite seu melhor email'
    )

    password1 = forms.CharField(
        label='Password 1',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        required=False,
        help_text='New Password'
    )

    password2 = forms.CharField(
        label='Password 2',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        required=False,
        help_text='Use the same password as before'
    )


    def save(self, commit=True):
        new_password = self.cleaned_data.get('password1')
        user = super().save(commit=False)

        if new_password:
            user.set_password(new_password)

        if commit:
            user.save()

        return user


    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        'Este email já está cadastrado',
                        code='invalid'
                    )
                )

        return email


    def clean_username(self):
        username = self.cleaned_data.get('username')
        current_username = self.instance.username

        if current_username != username:
            if User.objects.filter(username=username).exists():
                self.add_error(
                    'username',
                    ValidationError(
                        'Este username já está sendo usado',
                        code='invalid'
                    )
                )

        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))

        return password1
        

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', ValidationError('Senhas não batem', code='invalid'))

        return super().clean()
