import django_filters
from .models import Job, Location
from django import forms


class JobFilter(django_filters.FilterSet):
    job_location = django_filters.ModelChoiceFilter(
        queryset=Location.objects.all(),
        widget=forms.RadioSelect,
        empty_label="All",
        label='')
    

    class Meta:
        model = Job
        fields = ['job_location']
