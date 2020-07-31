from django.http import HttpResponse

def index(request):
    """ 
    La page d'index générique du projet 
    est géré par celle de l'appli "subsititute"
    """
    message = """Salut tout le monde !<br>
    Ici c'est la page d'index"""
    return HttpResponse(message)