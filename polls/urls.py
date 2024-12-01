from django.urls import path

from . import views

urlpatterns = [
    path("<int:year>/<int:month>", views.index, name="index"),
]