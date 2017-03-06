from django import forms
from users.models import JobOffer, JobPost, Company

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ('name', 'description', 'base_salary')

        widgets = {
            'name': forms.TextInput,
            'description': forms.Textarea,
            'base_salary': forms.NumberInput,
        }


class JobOfferForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        try:
            self.user = kwargs.pop('user')
        except:
            pass
        super(JobOfferForm, self).__init__(*args, **kwargs)

    class Meta:
        model = JobOffer
        fields = ('post', )

    def save(self, commit=True):
        job_offer = super(JobOfferForm, self).save(commit=False)
        job_offer.company = Company.objects.get(email=self.user.email)
        if commit:
            job_offer.save()
        return job_offer

