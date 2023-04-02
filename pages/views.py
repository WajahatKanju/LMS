from django.shortcuts import render
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

    # form_class = SettingsForm()
    context = {
    }

    def get(self, request):

        setting = Settings.objects.filter(employee__id__exact=self.request.user.id).first()
        form_class = SettingsForm(instance=setting)
        self.context['form'] = form_class
        print(self.request.user.id)
        return render(request, self.template_name, self.context)
