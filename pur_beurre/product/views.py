from django.http import HttpResponse
from django.shortcuts import render

def product(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur La page des products et des categories !</h1>
        <p>Les produits quoi !</p>
    """) 
    
def category (request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur La page des products et des categories !</h1>
        <p>Les categs quoi !</p>
    """)     