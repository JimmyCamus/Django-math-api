from django.urls import path
from . import views

urlpatterns = [
    path('fundamentals/derivate/', views.Derivate.as_view()),
    path('fundamentals/integrate/', views.Integrate.as_view()),
]

