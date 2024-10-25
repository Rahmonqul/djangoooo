from django.contrib import admin
from .models import ClientUser
from django.contrib.auth.admin import UserAdmin
from .form import CreateForm, ChangeForm
# Register your models here.

class ClientUserAdmin(UserAdmin):
    add_form = CreateForm
    form = ChangeForm
    model=ClientUser
    list_display = ["username","first_name", "last_name", "email", "age",  "manzil", "is_staff"]



admin.site.register(ClientUser, ClientUserAdmin)

