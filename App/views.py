from django.shortcuts import render, redirect
from App.models import Note
# Create your views here.
def home(request):
    if request.method == "POST":
        notes = request.POST.get('note')
        data = Note(notes = notes)
        data.save()
    sticky_notes = Note.objects.filter().all()
    note_dict = {
        "sticky_notes": sticky_notes
    }
    return render(request, 'index.html', note_dict)

def delete(request, note):
    note = Note.objects.filter(notes=note).delete()
    return redirect("/")