from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from student.models import Student
from student.forms import StudentForm
from school.models import Schools, Classes
from main.models import Settings


class StudentView(View):
    template_name = 'student/student.html'

    def get(self, request):
        schools = Schools.objects.all()
        classes = Classes.objects.all()

        school_id = request.GET.get('school')
        if school_id is None:
            try:
                setting = Settings.objects.get(employee__user_id__exact=self.request.user.id)
                school_id = setting.selected_school.id
            except Settings.DoesNotExist:
                school_id = request.GET.get('school')

        if school_id == 'all':
            school_id = None

        print(school_id)
        class_id = request.GET.get('class')

        if school_id and class_id:
            students = Student.objects.filter(grade__school_id=school_id, grade__classes_id=class_id)
        elif school_id:
            students = Student.objects.filter(grade__school_id=school_id)
        elif class_id:
            print(f'class id => {class_id}')
            students = Student.objects.filter(grade__classes_id=class_id)
        else:
            students = Student.objects.filter(active=True)

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

    def get(self, request, pk):
        return render(request, self.template_name, {'pk': pk})


class StudentDeleteView(LoginRequiredMixin, View):
    template_name = 'student/student_delete.html'

    def get(self, request, pk):
        return render(request, self.template_name, {'pk': pk})
