from django.shortcuts import render
from jobs.models import Job


def home(request):
    '''A view that displays the home page with a search bar'''
    jobs = Job.objects.all()

    return render(request, 'home.html', {'jobs': jobs})
