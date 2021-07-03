from django import forms

from .models import Usuario

class Userregisterform(forms.ModelForm):
    password1=forms.CharField(label='contraseña1',required=True,widget=forms.PasswordInput(
        attrs={'placeholder':'contraseña'}))
    password2 = forms.CharField(label='contraseña', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'repetir contraseña'}))
    class Meta:
        model= Usuario
        fields=(
            'username','email','nombres','apellidos','genero'
        )
        labels={
            'username':'Nombre usuario'
        }
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')

class Loginform(forms.Form):
    username=forms.CharField(label='username',required=True,widget=forms.TextInput(attrs={'placeholder':'username',
                                                                                          'style':'{margin:10px}'}))
    password = forms.CharField(label='contraseña', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'contraseña'}))
