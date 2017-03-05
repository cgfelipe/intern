from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from users.forms import *
from django.views import View
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'users/home.html')


class SignupView(View):
    forms = {
        'student': StudentCreationForm,
        'school': SchoolCreationForm,
        'company': CompanyCreationForm,
    }

    def post(self, request, account_type):
        form = self.forms.get(account_type)(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successfully completed!')
            return render(request, 'users/home.html', locals())
        else:
            return render(request, 'users/signup.html', locals())

    def get(self, request, account_type):
        form = self.forms.get(account_type)()
        return render(request, 'users/signup.html', locals())



class LoginView(View):
    form = LoginForm

    def get(self, request):
        form = self.form()
        return render(request, 'users/login.html', locals())

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            auth.login(request, user)
            messages.success(request, 'Welcome, {0}!'.format(form.cleaned_data['email']))
            return render(request, 'jobs/index.html', locals())
        else:
            return render(request, 'users/login.html', locals())
