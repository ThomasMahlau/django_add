from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .filters import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def entry(request):
    apps = Navigation.objects.all()
    ctx = {'apps': apps}
    return render(request, 'entry.html', ctx)

def mitarbeiter_list(request):
    mitarbeiterinnen = Mitarbeiter.objects.all()
    ctx = {'mitarbeiterinnen': mitarbeiterinnen}
    return render(request, 'mitarbeiter_list.html', ctx)

def mitarbeiter_list_filter(request):  
        mitarbeiter_filter = MitarbeiterFilter(
            request.GET, 
            queryset=Mitarbeiter.objects.all()
        )
        ctx = {"mitarbeiterinnen": mitarbeiter_filter.qs,
            "mitarbeiter_filter": mitarbeiter_filter}

        return render(request, "mitarbeiter_list_filter.html", ctx)

def mitarbeiter_detail(request, id):
    mitarbeiter = Mitarbeiter.objects.get(id = id)
    ctx = {'mitarbeiter': mitarbeiter}
    return render(request, 'mitarbeiter_detail.html', ctx)

def mitarbeiter_update(request, id):
    mitarbeiter = Mitarbeiter.objects.get(id = id)
    ctx = {'mitarbeiter': mitarbeiter}
    return render(request, 'mitarbeiter_update.html', ctx)

def loginSeite(request):
    if request.method == 'POST':
        benutzername = request.POST['benutzername']
        passwort = request.POST['passwort']
        
        benutzer = authenticate(request, username=benutzername, password=passwort)
        
        if benutzer is not None:
            login(request, benutzer)
            messages.success(request, 'Sie sind erfolgreich eingeloggt!')
            return redirect('entry')
        else:
            messages.error(request, 'Falscher Benutzername oder Passwort')
        
    return render(request, 'login.html')

def logoutBenutzer(request):
    logout(request)     # Session-Cockie wird gelöscht
    messages.success(request, 'Sie haben sich erfolgreich ausgeloggt!')
    return redirect('entry')

def registerx(request):
    if request.method == "POST":
        form = MitarbeiterRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Mitarbeiter wurde erfolgreich erstellt")
            return redirect("mitarbeiter_list.html")
    else:
        form = MitarbeiterRegisterForm()
    ctx = {"form": form}
    return render(request, "mitarbeiter_form.html", ctx)

def register(request):
    seite = 'reg'
    form = EigeneUserCreationForm

    if request.method == 'POST':
        form = EigeneUserCreationForm(request.POST)
        if form.is_valid():
            benutzer = form.save(commit=False)
            benutzer.save()

            mitarbeiter=Mitarbeiter(name=request.POST['username'], benutzer=benutzer)
            mitarbeiter.save()
            
            login(request, benutzer)
            return redirect('mitarbeiter_list')
        else:
            messages.error(request, "Fehlerhafte Eingabe!")    

    ctx = {'form': form, 'seite': seite }
    return render(request, 'mitarbeiter_form.html', ctx)