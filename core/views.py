from django.shortcuts import render
from jobs.filters import JobFilter
from jobs.models import Job


def home(request):
    '''A view that displays the home page with a search bar'''
    jobs = Job.objects.all()
    filtered_jobs = JobFilter(request.GET, queryset=jobs)

    return render(request, 'home.html', {'filter': filtered_jobs})
