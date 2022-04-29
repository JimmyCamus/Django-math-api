from django.urls import path
from . import views

urlpatterns = [
    path('numericalmethods/bisection/', views.BisectionMethod.as_view()),
    path('numericalmethods/newthon-raphson/', views.NewtonRaphsonMethod.as_view()),
]

