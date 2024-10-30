# fitness_tracker/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Fitness Tracker!")
