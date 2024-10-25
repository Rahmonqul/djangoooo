from django.contrib.auth.forms import forms, UserCreationForm, UserChangeForm
from .models import ClientUser


class CreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = ClientUser
        fields = ("username", 'last_name', 'first_name', 'email',"age")


class ChangeForm(UserChangeForm):
    class Meta:
        model = ClientUser
        fields = ("username", 'last_name', 'first_name', 'email',"age")
