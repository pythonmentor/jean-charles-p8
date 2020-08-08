from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from user.forms import CustomUserCreationForm


# users/views.py


def dashboard(request):
    return render(request, "user/dashboard.html")


def user(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur lapage des users !</h1>
        <p>Les utilisateurs quoi !</p>
    """)
            

def register(request):
    if request.method == "GET":
        return render(
            request, "user/register.html",
            {"form": CustomUserCreationForm}
        )

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))