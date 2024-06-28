from django.urls import path
from . import views

urlpatterns = [
    path("", views.pre_base_view, name="pre_base"),
    path("<str:lan>/", views.base_view, name="base"),
    path("company/<str:lan>/", views.company_view, name="company"),
    path("solutions/<str:lan>/", views.solutions_view, name="solutions"),
    path("contact-us/<str:lan>/", views.contact_us_view, name="contact_us"),
    path("category/<int:id>/<str:lan>/", views.category_view, name="category"),
    path("product/<int:id>/<str:lan>/", views.product_view, name="product"),
]
