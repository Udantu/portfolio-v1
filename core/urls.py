from django.urls import path
from . import views as core_views

urlpatterns = [
    path('',core_views.index,name="toHome"),
    path('about/',core_views.about,name="toAbout"),
    path('dashboard/',core_views.dashboard,name="toDashboard"),
]
