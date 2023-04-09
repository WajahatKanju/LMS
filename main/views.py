from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View

from django.http import JsonResponse
from school.models import SchoolClasses


class HomeView(View):
    template_name = 'main/index.html'

    context = {'title': 'School Management System', }

    def get(self, request):
        return render(request, self.template_name, self.context)


def get_grades(request, school_id):
    grades = SchoolClasses.objects.filter(school_id=school_id).values('id', 'classes', 'classes__name', 'school__name')
    grades_dict = {
        grade['id']: {'id': grade['classes'], 'name': (grade['classes__name'] + " - " + grade['school__name'])} for
        grade in grades}
    print(f'grades dict {grades_dict}')
    return JsonResponse(grades_dict)
