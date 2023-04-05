from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from student.models import Student
from student.forms import StudentForm


class StudentView(View):
    template_name = 'student/student.html'

    context = {

    }

    def get(self, request):
        self.context['students'] = Student.objects.filter(active=True)
        return render(request, self.template_name, self.context)


class StudentDetailView(View):
    template_name = 'student/student_detail.html'

    def get(self, request, pk):
        return render(request, self.template_name, {'pk': pk})


class StudentCreateView(LoginRequiredMixin, View):
    template_name = 'student/student_form.html'
    success_url = 'student:all'

    def get(self, request):
        form = StudentForm(prefix='student')
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = StudentForm(request.POST, prefix='student')
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = {'form': form}
        return render(request, self.template_name, context)


class StudentUpdateView(LoginRequiredMixin, View):
    template_name = 'student/student_form.html'

    def get(self, request, pk):
        return render(request, self.template_name, {'pk': pk})


class StudentDeleteView(LoginRequiredMixin, View):
    template_name = 'student/student_delete.html'

    def get(self, request, pk):
        return render(request, self.template_name, {'pk': pk})
