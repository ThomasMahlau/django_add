from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *

# LISTEN
# MIT FILTER
"""
def mitarbeiter_list_filter(request):
    mitarbeiter_filter = MitarbeiterFilter(
        request.GET, queryset=Mitarbeiter.objects.all()
    )
    ctx = {"filter": mitarbeiter_filter}
    return render(request, "mitarbeiter_list.html", ctx)
"""

# OHNE FILTER
def mitarbeiter_list(request):
    mitarbeiterinnen = Mitarbeiter.objects.all()
    ctx = {'mitarbeiterinnen': mitarbeiterinnen}
    return render(request, 'mitarbeiter_list.html', ctx)

# UPDATEN
def mitarbeiter_update(request, id: int):
    mitarbeiter = Mitarbeiter.objects.get(id=id)
    if request.method == "POST":
        form = MitarbeiterForm(request.POST, instance=mitarbeiter)
        if form.is_valid():
            form.save()
            messages.success(request, "Mitarbeiter wurde erfolgreich aktualisiert.")
            return redirect("mitarbeiter_list")
    else:
        form = MitarbeiterForm(instance=mitarbeiter)
    context = {"form": form, "mitarbeiter": mitarbeiter}
    return render(request, "mitarbeiter_form.html", context)

# DELETE
def mitarbeiter_delete(request, id : int):
    mitarbeiter = Mitarbeiter.objects.get(id=id)
    if request.method == "POST":
        mitarbeiter.delete()
        messages.success(request, "Mitarbeiter wurde erfolgreich gelöscht.")
        return redirect("mitarbeiter_list")
    context = {"mitarbeiter": mitarbeiter}
    return render(request, "mitarbeiter_list.html", context)

# CREATE
def mitarbeiter_create(request):
    if request.method == "POST":
        form = MitarbeiterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Mitarbeiter wurde erfolgreich erstellt.")
            return redirect("mitarbeiter_list")
    else:
        form = MitarbeiterForm()
    context = {"form": form}
    return render(request, "/mitarbeiter_form.html", context)