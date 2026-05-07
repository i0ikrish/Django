from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from .models import Document
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def home(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('home')
    else:
        form = NoteForm()

    notes = Note.objects.filter(user=request.user)

    return render(request, 'core/home.html', {
        'notes': notes,
        'form': form
    })


@login_required
def edit_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)

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

@login_required
def delete_note(request,id):
    note = get_object_or_404(Note, id=id, user=request.user)
    note.delete()
    return redirect('home')

@login_required
def upload_pdf(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = request.user
            doc.save()
            return redirect('upload_pdf')
    else:
        form = DocumentForm()

    documents = Document.objects.filter(user=request.user)

    return render(request, 'core/upload_pdf.html', {
        'form': form,
        'documents': documents
    })