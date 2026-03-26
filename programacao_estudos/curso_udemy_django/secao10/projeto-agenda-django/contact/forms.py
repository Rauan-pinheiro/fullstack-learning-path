from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class ContactForm(forms.ModelForm):
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'aceppt': 'iamge/*',
            }
        )
    )
        
    
    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
        )
        
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name =  cleaned_data.get('first_name')
        last_name =  cleaned_data.get('last_name')
        
        if first_name == last_name:
            
            msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo erro',
                    code='invalid'
                )
            
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'veio do add_erro',
                    code='invalid'
                )
            )
        
        return first_name
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField( # verificação do campo 'primeiro nome', 'required=True' significa que o campo não pode ser vazio
        required=True,
        min_length=3, # mínimo de caracteres
    )
    
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    
    email = forms.EmailField()
    
    class Meta: # Define os campos do formulário
        model = User
        
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        )
        
    # está função faz a validação se um email já existir no cadastro de algum usuário(email em uso)
    def clean_email(self): 
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', # campo 'email'
                ValidationError('Já existe este e-mail', code='invalid') # mensagem de erro
            )
            
        return email