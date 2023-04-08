from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.urls import reverse, reverse_lazy
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from student.models import Student
from student.forms import StudentForm
from school.models import Schools, Classes


class StudentView(View):
    template_name = 'student/student.html'

    def get(self, request):
        schools = Schools.objects.all()
        classes = Classes.objects.all()

        school_id = request.GET.get('school')
        gender = request.GET.get('gender')
        class_id = request.GET.get('class')
        query = request.GET.get('search')

        if query:
            students = Student.objects.filter(
                Q(name__icontains=query) | Q(roll_no__icontains=query) | Q(admission_no__icontains=query) | Q(
                    student_cnic__icontains=query) | Q(father_cnic__icontains=query) | Q(
                    mobile__icontains=query)).distinct()

        elif school_id and class_id:
            students = Student.objects.filter(grade__school_id=school_id, grade__classes_id=class_id)

        elif school_id:
            students = Student.objects.filter(grade__school_id=school_id)

        elif class_id:
            students = Student.objects.filter(grade__classes_id=class_id)

        elif gender:
            students = Student.objects.filter(gender=gender)
        else:
            students = Student.objects.all()

        context = {'students': students, 'schools': schools, 'classes': classes,
                   'selected_school': school_id if school_id else None,
                   'selected_class': class_id if class_id else None, }

        return render(request, self.template_name, context)


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

    success_url = 'student:all'
    context = {'form_title': 'Update Student'}

    def get(self, request, pk):
        student = get_object_or_404(Student, roll_no=pk)
        form = StudentForm(instance=student)
        self.context['form'] = form
        self.context['pk'] = pk
        return render(request, self.template_name, self.context)

    def post(self, request, pk):
        student = get_object_or_404(Student, roll_no=pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        self.context['form'] = form
        return render(request, self.template_name, self.context)


class StudentDeleteView(LoginRequiredMixin, View):
    template_name = 'delete.html'
    success_url = reverse_lazy('student:all')

    context = {}

    def get(self, request, pk):
        student = get_object_or_404(Student, roll_no=pk)

        self.context['object'] = student
        return render(request, self.template_name, self.context)

    def post(self, request, pk=None):
        student = get_object_or_404(Student, roll_no=pk)
        student.active = False
        student.save()
        messages.success(request, 'Student has been deleted')

        return redirect(self.success_url)
