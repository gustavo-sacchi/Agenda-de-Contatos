from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm

from .models import UserPersonalizado


@admin.register(UserPersonalizado)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = UserPersonalizado
    # Agora Personalizando
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ("biografia", "foto_perfil",)}),
    )