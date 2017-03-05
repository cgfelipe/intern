from django.forms import Form
from django.contrib.auth.models import Permission
from users.admin import *
from users.models import *

class StudentCreationForm(EntityCreationForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'street', 'neighborhood', 'city', 'cpf', 'date_of_birth', 'school_vinculation')

    def save(self, commit=True):
        student = super(StudentCreationForm, self).save(commit=False)
        student.set_password(self.cleaned_data['password1'])
        student.is_student = True
        if commit:
            student.save()
        return student


class SchoolCreationForm(EntityCreationForm):
    class Meta:
        model = School
        fields = ('name', 'email', 'street', 'neighborhood', 'city', 'cnpj', 'short_name')

    def save(self, commit=True):
        school = super(SchoolCreationForm, self).save(commit=False)
        school.set_password(self.cleaned_data['password1'])
        school.is_school = True
        if commit:
            school.save()
        return school


class CompanyCreationForm(EntityCreationForm):
    class Meta:
        model = Company
        fields = ('name', 'email', 'street', 'neighborhood', 'city', 'cnpj')

    def save(self, commit=True):
        company = super(CompanyCreationForm, self).save(commit=False)
        company.set_password(self.cleaned_data['password1'])
        company.is_company = True
        if commit:
            company.save()
        return company


class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail Address', widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)