from django.http import HttpResponse
from django.shortcuts import render

def user(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur lapage des users !</h1>
        <p>Les utilisateurs quoi !</p>
    """)