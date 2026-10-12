from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label="Full name")
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'username', 'email')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'priority')