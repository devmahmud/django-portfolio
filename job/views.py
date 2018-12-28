from django.shortcuts import render
from .models import Job


def index(request):
    jobs = Job.objects.all()
    return render(request, 'job/home.html', {'jobs': jobs})
