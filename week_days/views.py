from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def day_ned(request, day: str):
    if day == "monday":
        return HttpResponse("Понедельник день тяжелый")
    elif day == "tuesday":
        return HttpResponse("Вторник полная версия понедельника")


def day_ned_num(request, day: int):
    if 1 <= day <= 7:
        return HttpResponse(f"Сегодня {day} день недели")
    else:
        return HttpResponse(f"Вы ввели неправильный день - {day}")
