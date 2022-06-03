from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NoteCreationForm


@login_required
def notes(request):
    author = request.user
    user_notes = author.notes_set.all()
    context = {'notes': user_notes}
    return render(request, 'notes/notes.html', context)


@login_required
def note_detail(request, pk):
    author = request.user
    user_note = author.notes_set.get(id=pk)
    context = {'note': user_note}
    return render(request, 'notes/note.html', context)


@login_required
def add_note(request):
    author = request.user
    if request.method == 'POST':
        form = NoteCreationForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = author
            note.save()
            return redirect('notes')
    else:
        form = NoteCreationForm()
    context = {'form': form}
    return render(request, 'notes/note_form.html', context)


@login_required
def update_note(request, pk):
    author = request.user
    note = author.notes_set.get(id=pk)
    if request.method == 'POST':
        form = NoteCreationForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteCreationForm(instance=note)
    context = {'form': form}
    return render(request, 'notes/note_form.html', context)


@login_required
def delete_note(request, pk):
    author = request.user
    note = author.notes_set.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    context = {'note': note}
    return render(request, 'notes/delete_note.html', context)
