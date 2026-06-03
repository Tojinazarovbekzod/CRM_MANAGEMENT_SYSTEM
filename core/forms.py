from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="Ism", widget=forms.TextInput(attrs={'placeholder': 'Ismingiz'}))
    last_name = forms.CharField(max_length=100, label="Familiya", widget=forms.TextInput(attrs={'placeholder': 'Familiyangiz'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def clean(self):
        cleaned = super().clean()
        first_name = cleaned.get('first_name', '').strip()
        last_name = cleaned.get('last_name', '').strip()
        if first_name and last_name:
            if User.objects.filter(first_name__iexact=first_name, last_name__iexact=last_name).exists():
                raise forms.ValidationError(
                    f"'{first_name} {last_name}' ismi bilan foydalanuvchi allaqachon mavjud."
                )
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name'].strip()
        user.last_name = self.cleaned_data['last_name'].strip()
        if commit:
            user.save()
        return user
