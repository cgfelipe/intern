"""intern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including anotsther URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import users.views
import jobs.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', users.views.home, name='index'),
    url(r'^signup/(\w+)/$', users.views.SignupView.as_view(), name='signup'),
    url(r'^login/$', users.views.LoginView.as_view(), name='login'),
    url(r'^jobs/$', jobs.views.IndexView.as_view(), name='index'),
    url(r'^jobs/new_post/$', jobs.views.JobPostView.as_view(), name='new_job_post'),
    url(r'^jobs/new_offer/$', jobs.views.JobAnnouncementView.as_view(), name='new_job_offer')
]
