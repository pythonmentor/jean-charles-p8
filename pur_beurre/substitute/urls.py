from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index), #

#    path(r'^$', include(('substitute.urls','substitute'), namespace='substitute')),
#    path(r'^substitute/', include(('substitute.urls','substitute'), namespace='substitute')),
#    path(r'^$', views.listing, name='listing'),
]
