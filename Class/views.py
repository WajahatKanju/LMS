from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ClassForm
from django.urls import reverse_lazy

from .models import Class


class ClassView(ListView):
    model = Class
    template_name = 'Class/class_list.html'
    context_object_name = 'classes'


class ClassDetailView(DetailView):
    model = Class
    template_name = 'Class/class_detail.html'
    context_object_name = 'class'


class ClassCreateView(CreateView):
    model = Class
    template_name = 'Class/class_form.html'
    form_class = ClassForm
    success_url = reverse_lazy('class:all')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ClassUpdateView(UpdateView):
    model = Class
    template_name = 'Class/class_form.html'
    form_class = ClassForm
    success_url = reverse_lazy('class:all')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ClassDeleteView(DeleteView):
    model = Class
    template_name = 'class/class_confirm_delete.html'
    context_object_name = 'class'
    success_url = reverse_lazy('class:all')
