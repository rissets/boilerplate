from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Dashboard

class HomeView(View):
    def get(self, request):
        greeting = {'title': "Home", 'pageview': "Boilerplate"}
        return render(request, 'pages/index.html', greeting)

def error_handler(request, filename):
    return render(request, filename, {}, content_type='text/html')


def error_403(request, exception):
    return render(request, '403.html', {}, content_type='text/html')


def error_404(request, exception):
    return render(request, '404.html', {}, content_type='text/html')


def error_500(request):
    return render(request, '500.html', {}, content_type='text/html')
