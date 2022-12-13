from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


# Create your views here.
class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        print(request.session)
        greeting = {'title': "Dashboard", 'pageview': "Boilerplate"}
        return render(request, 'menu/index.html', greeting)