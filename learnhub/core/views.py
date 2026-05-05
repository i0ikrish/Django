from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


# Create your views here.



def home(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()

    notes = Note.objects.all()

    return render(request, 'core/home.html', {
        'notes': notes,
        'form': form
    })
def edit_note(request, id):
    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)

    return render(request, 'core/edit_note.html', {
        'form': form
    })