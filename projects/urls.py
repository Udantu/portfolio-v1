from django.urls import path
from . import views as projects_views
from .views import ProgramDetailView

urlpatterns = [
    path('', projects_views.program, name="toProjects"),
    path('project=<int:pk>/', ProgramDetailView.as_view(), name="toProgramDetail"),
    path('ComPro_STA257/',projects_views.compro_time_series),
    path('ComPro_CSC356/',projects_views.compro_factor_analysis)
]
