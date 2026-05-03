from django.shortcuts import render
from django.http import HttpResponse
from .models import Note


# Create your views here.




def home(request):
    notes = Note.objects.all()
    return render(request, 'core/home.html', {
        'notes': notes
    })