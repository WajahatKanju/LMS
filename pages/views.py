from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View

from main.form import SettingsForm
from main.models import Settings


class HomeView(View):
    template_name = 'pages/index.html'

    context = {
        'school': 'GHSS CHITOR'
    }

    def get(self, request):

        return render(request, self.template_name, self.context)


class SettingsView(View):
    template_name = 'pages/settings.html'
    success_url = reverse_lazy('settings')

    # form_class = SettingsForm()
    context = {
        'form': SettingsForm(),
        'errors': [],
    }

    def get(self, request):

        setting = Settings.objects.filter(employee__id__exact=self.request.user.id).first()
        form = SettingsForm(instance=setting)
        self.context['form'] = form
        print(self.request.user.id)
        return render(request, self.template_name, self.context)

    def post(self, request,):
        setting = Settings.objects.filter(employee__id__exact=self.request.user.id).first()
        form = SettingsForm(request.POST, instance=setting)
        if form.is_valid():
            form.save(commit=False)
            form.employee = self.request.user
            form.save()

            return redirect(self.success_url)

        self.context['errors'].append({'type': 'error Type', 'message': 'Invalid'})
        return redirect(self.success_url)
