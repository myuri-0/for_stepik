from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.
from django.views import View
from app_tours import data


class MainView(View):

    def get(self, request):
        return render(request, 'index.html')


class DepartureView(View):

    def get(self, request, departure):

        if departure not in data.departures.keys():
            raise Http404
        return render(request, 'departure.html')


class TourView(View):

    def get(self, request, id):

        if id not in data.tours.keys():
            raise Http404
        context = data.tours[id]
        return render(request, 'tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Page not found 404! Такой страницы не существует!')
