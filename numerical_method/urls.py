from django.urls import path
from . import views

urlpatterns = [
    path('numericalmethods/bisection/', views.BisectionMethod.as_view()),
    path('numericalmethods/newthon-raphson/',
         views.NewtonRaphsonMethod.as_view()),
    path('numericalmethods/fixed-point/', views.FixedPointMethod.as_view()),
]
