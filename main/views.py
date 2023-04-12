from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View




class HomeView(View):
    template_name = 'main/index.html'

    context = {'title': 'School Management System', }

    def get(self, request):
        return render(request, self.template_name, self.context)


