from django.urls import path
from . import views

urlpatterns = [
    path("", views.base_view, name="base"),
    path("company/", views.company_view, name="company"),
    path("solutions/", views.solutions_view, name="solutions")
]
