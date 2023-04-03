from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView, DeleteView
from django.views.decorators.cache import never_cache

from main.form import SettingsForm, SchoolForm
from main.models import Settings, Schools


class HomeView(View):
    template_name = 'main/index.html'

    context = {}

    def get(self, request):
        setting = Settings.objects.get(employee__user_id__exact=self.request.user.id)
        self.context['select_school'] = setting.selected_school
        return render(request, self.template_name, self.context)


class SettingsView(View):
    template_name = 'main/settings.html'
    success_url = reverse_lazy('settings')

    # form_class = SettingsForm()
    context = {'form': SettingsForm(), 'errors': [], }

    def get(self, request):
        setting = Settings.objects.get(employee__user_id__exact=self.request.user.id)
        form = SettingsForm(instance=setting)
        self.context['form'] = form
        print(self.request.user.id)
        return render(request, self.template_name, self.context)

    def post(self, request, ):
        setting = Settings.objects.get(employee__user_id__exact=self.request.user.id)
        form = SettingsForm(request.POST, instance=setting)
        if form.is_valid():
            form.save(commit=False)
            form.employee = self.request.user
            form.save()

            return redirect(self.success_url)

        self.context['errors'].append({'type': 'error Type', 'message': 'Invalid'})
        return redirect(self.success_url)


@method_decorator(never_cache, name='dispatch')
class SchoolView(ListView):
    template_name = 'school/school.html'
    schools = Schools.objects.all()
    context = {'schools': schools}

    def get(self, request, **kwargs):
        setting = Settings.objects.get(employee__user_id__exact=self.request.user.id)
        self.context['select_school'] = setting.selected_school
        return render(request, self.template_name, self.context)


class SchoolDetailView(View):
    template_name = 'school/school_detail.html'
    context = {}

    def get(self, request, pk=None):
        school = get_object_or_404(Schools, id=pk)
        self.context['school'] = school
        setting = Settings.objects.get(employee__user_id__exact=self.request.user.id)
        self.context['select_school'] = setting.selected_school

        return render(request, self.template_name, self.context)


class SchoolCreateView(View):
    template_name = 'school/school_create.html'

    context = {}

    def get(self, request):
        form = SchoolForm()
        self.context['form'] = form
        setting = Settings.objects.get(employee__user_id__exact=self.request.user.id)
        self.context['select_school'] = setting.selected_school
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect(reverse_lazy('school'))

        self.context['form'] = form
        return render(request, self.template_name, self.context)


class SchoolUpdateView(View):
    template_name = 'school/school_create.html'
    context = {}

    def get(self, request, pk=None):
        school = get_object_or_404(Schools, id=pk)
        form = SchoolForm(instance=school)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        school = get_object_or_404(Schools, id=pk)
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect(reverse_lazy('school'))

        self.context['form'] = form
        return render(request, self.template_name, self.context)


class SchoolDeleteView(View):

    template_name = 'school/school_delete.html'

    context = {}

    def get(self, request, pk=None):
        school = get_object_or_404(Schools, id=pk)
        form = SchoolForm(instance=school)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        school = get_object_or_404(Schools, id=pk)
        school.active = False
        school.save()
        messages.success(request, 'Form submission successful')
        # form = SchoolForm(request.POST, instance=school)
        # if form.is_valid():
        #     school.active = False
        #     form.save()
        #     messages.success(request, 'Form submission successful')
        #     return redirect(reverse_lazy('school'))
        # print(form.errors)
        # self.context['form'] = form
        return redirect(reverse_lazy('school'))
