from random import sample

from django.http import HttpResponseNotFound, Http404, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from app_tours import data


class MainView(View):

    def get(self, request):
        rand_tour = sample(range(1, 17), k=6)
        context = {
            "departures": data.departures,
            "tours": data.tours,
            "random_tour": rand_tour
        }
        return render(request, 'index.html', context=context)


class DepartureView(View):

    def get(self, request, departure):
        if departure not in data.departures.keys():
            raise Http404
        
        context = {
            "departures": data.departures,
            "tours": data.tours,
        }
        return render(request, 'departure.html', context=context)


class TourView(View):

    def get(self, request, id):
        if id not in data.tours.keys():
            raise Http404
        context = {
            "departures": data.departures,
            "tours": data.tours
        }
        return render(request, 'tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Page not found 404! Такой страницы не существует!')


def custom_handler500(request):
    return HttpResponseServerError('Internal Server Error 500! Внутренняя ошибка сервера!')
