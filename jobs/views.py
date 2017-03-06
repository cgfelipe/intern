from django.shortcuts import render
from django.views import View
from .forms import JobPostForm, JobOfferForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from users.models import JobOffer

# Create your views here.
class IndexView(View):
    job_post_form = JobPostForm
    job_announcement_form = JobOfferForm

    def get(self, request):
        job_list = JobOffer.objects.all()
        job_post_form = self.job_post_form()
        job_announcement_form = self.job_announcement_form()
        return render(request, 'jobs/index.html', locals())


class JobPostView(IndexView):

    def post(self, request):
        job_post = self.job_post_form(request.POST)
        if job_post.is_valid():
            job_post.save()
            messages.success(request,
                             '{0} successfully registered as a job post.'.format(job_post.cleaned_data.get('name')))
        else:
            messages.error(request, job_post.errors)
        return HttpResponseRedirect('/jobs/')


class JobAnnouncementView(IndexView):
    def post(self, request):
        job_announce = self.job_announcement_form(request.POST, user=request.user)
        if job_announce.is_valid():
            job_announce.save()
            messages.success(request,
                             'Internship offer successfully registered.')
        else:
            messages.error(request, job_announce.errors)
        return HttpResponseRedirect('/jobs/')


