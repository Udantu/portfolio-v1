from django.urls import path
from . import views as survey_views

urlpatterns = [
    path('', survey_views.survey, name="toSurvey"),
    path('<int:id>/', survey_views.take_survey, name="toTakeSurvey")
]
