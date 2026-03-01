from django import forms
from .models import CustomUser 

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser 
        fields = ['username', 'email', 'password', 'is_staff', 'is_superuser', 'is_admin', 'profile_picture', 'phone_number']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'accept': 'image/*'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_admin': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),

        }


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)