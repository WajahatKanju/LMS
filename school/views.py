from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View

from main.models import Settings
from .forms import SchoolForm
from .models import Schools


# Create your views here.
class SchoolView(ListView):
    template_name = 'school/school.html'

    context = {}

    def get(self, request, **kwargs):

        self.context['schools'] = Schools.objects.filter(active=True)
        return render(request, self.template_name, self.context)


class SchoolDetailView(View):
    template_name = 'school/school_detail.html'
    context = {}

    def get(self, request, pk=None):
        school = get_object_or_404(Schools, id=pk)
        self.context['school'] = school

        return render(request, self.template_name, self.context)


class SchoolCreateView(View):
    template_name = 'school/school_create.html'

    context = {}

    def get(self, request):
        form = SchoolForm()
        self.context['form'] = form

        return render(request, self.template_name, self.context)

    def post(self, request):
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect(reverse_lazy('school:all'))

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
            return redirect(reverse_lazy('school:all'))

        self.context['form'] = form
        return render(request, self.template_name, self.context)


class SchoolDeleteView(View):

    template_name = 'school/school_delete.html'
    success_url = reverse_lazy('school:all')
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

        return redirect(self.success_url)
