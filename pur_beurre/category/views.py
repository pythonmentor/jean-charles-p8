from django.http import HttpResponse
from django.shortcuts import render

def category(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur la page des categories !</h1>
        <p>Les categories quoi !</p>
    """)