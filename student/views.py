from django.shortcuts import render, redirect
from django.views.generic import View

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


class StudentCreateView(View):
    template_name = 'student/student_form.html'
    success_url = 'student:all'

    context = {
        'form': StudentForm()
    }

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)


class StudentUpdateView(View):
    template_name = 'student/student_form.html'

    def get(self, request, pk):
        return render(request, self.template_name, {'pk': pk})


class StudentDeleteView(View):
    template_name = 'student/student_delete.html'

    def get(self, request, pk):
        return render(request, self.template_name, {'pk': pk})
