from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.product), #
    path('product', views.product), #
    path('category', views.category), #
]
