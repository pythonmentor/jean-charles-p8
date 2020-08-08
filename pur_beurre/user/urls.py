from django.urls import path, include
from .views import dashboard, user
# from user.views import dashboard

urlpatterns = [
    path(r"dashboard/", dashboard, name="dashboard"),
    path(r"accounts/", include("django.contrib.auth.urls")),
    path(r"user/", user, name="user"), #
]
