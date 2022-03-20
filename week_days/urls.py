from django.urls import path
from . import views

urlpatterns = [

    path('<int:day>/', views.day_ned_num),
    path('<str:day>/', views.day_ned),

]