from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from users.models import *

# Register your models here.
from users.models import Entity


class EntityCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        entity = super(EntityCreationForm, self).save(commit=False)
        entity.set_password(self.cleaned_data['password1'])
        if commit:
            entity.save()
        return entity


class EntityChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Entity
        fields = ('name', 'email', 'street', 'neighborhood', 'city', 'is_admin', 'is_active')

    def clean_password(self):
        return self.initial['password']


class EntityAdmin(BaseUserAdmin):
    form = EntityChangeForm
    add_form = EntityCreationForm

    list_display = ('name', 'email', 'street', 'neighborhood', 'city', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Entity Informations', {'fields': ('name', 'street', 'neighborhood', 'city')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'street', 'neighborhood', 'city', 'password1', 'password2')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Entity, EntityAdmin)