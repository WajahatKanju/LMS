from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SettingsForm
from .models import Settings, Employee
from school.models import Schools

from django.http import JsonResponse
from school.models import SchoolClasses


class HomeView(View):
    template_name = 'main/index.html'

    context = {
        'title': 'School Management System',
    }

    def get(self, request):

        return render(request, self.template_name, self.context)


class SettingsView(LoginRequiredMixin, View):
    template_name = 'main/settings.html'
    success_url = reverse_lazy('settings')

    # form_class = SettingsForm()
    context = {'form': SettingsForm(), 'errors': [], }
    user = None

    def get(self, request):
        try:
            setting = Settings.objects.get(employee__user_id__exact=self.request.user.id)
            form = SettingsForm(instance=setting)
        except Settings.DoesNotExist:
            form = SettingsForm()
        self.context['form'] = form
        print(self.request.user.id)
        return render(request, self.template_name, self.context)

    def post(self, request, ):
        try:
            setting = Settings.objects.get(employee__user_id__exact=self.request.user.id)
            form = SettingsForm(request.POST, instance=setting)
        except Settings.DoesNotExist:
            form = SettingsForm(request.POST)
            self.user = Employee(user=self.request.user, designation='Teacher',
                                 school=Schools.objects.get(id=request.POST.get('selected_school')), active=True)
            self.user.save()

        if form.is_valid():
            setting = form.save(commit=False)
            if self.user:
                setting.employee = self.user
            else:
                setting.employee = Employee.objects.get(user=self.request.user)
            setting.save()

            return redirect(self.success_url)

        self.context['errors'].append({'type': 'error Type', 'message': 'Invalid'})
        return redirect(self.success_url)


def get_grades(request, school_id):
    grades = SchoolClasses.objects.filter(school_id=school_id).values('id', 'classes', 'classes__name', 'school__name')
    grades_dict = {grade['id']: {'id': grade['classes'], 'name': (grade['classes__name'] + " - " + grade['school__name'])} for
                   grade in grades}
    print(f'grades dict {grades_dict}')
    return JsonResponse(grades_dict)
