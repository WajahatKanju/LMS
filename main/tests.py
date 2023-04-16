from django.test import TestCase, Client
from django.urls import reverse
from student.models import Student
from school.models import SchoolClasses
from student.forms import StudentForm
import json

import uuid
from django.urls import reverse
from django.test import TestCase


class TestGuestViews(TestCase):

    def test_homepage(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'School Management System')
        self.assertTemplateUsed(response, 'main/index.html')

    def test_signup(self):
        url = reverse('account_signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_login(self):
        url = reverse('account_login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_settings_page(self):
        url = reverse('settings')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_student(self):
        url = reverse('student:all')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_student_create(self):
        url = reverse('student:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_student_update(self, pk=1):
        url = reverse('student:update', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_student_delete(self, pk=1):
        url = reverse('student:delete', args=[pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_school(self):
        url = reverse('school:all')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'school/school_list.html')

    def test_school_create(self):
        url = reverse('school:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_school_update(self, pk=uuid.uuid4()):
        url = reverse('school:update', args=[str(pk)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_school_delete(self, pk=uuid.uuid4()):
        url = reverse('school:delete', args=[str(pk)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class GetGradesViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.school_class1 = SchoolClasses.objects.create(id=1, classes='Class A', name='School A')
        self.school_class2 = SchoolClasses.objects.create(id=2, classes='Class B', name='School B')

    def test_get_grades_view(self):
        url = reverse('get_grades', args=[self.school_class1.school_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
            {"1": {"id": "Class A", "name": "Class A - School A"}, })


class RegisterStudentViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.school_class1 = SchoolClasses.objects.create(id=1, classes='Class A', name='School A')
        self.form_data = {'student-roll_no': '123', 'student-admission_no': '1234',
            'student-date_of_birth': '2020-01-01', 'student-admission_date': '2021-01-01', 'student-name': 'John Doe',
            'student-father_name': 'Bob Doe', 'student-student_cnic': '1234567890', 'student-father_cnic': '0987654321',
            'student-gender': 'M', 'student-mobile': '1234567890', 'student-school': self.school_class1.school_id,
            'student-grade': self.school_class1.id, }

    def test_register_student_view_with_valid_data(self):
        url = reverse('register_student')
        response = self.client.post(url, data=self.form_data)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"success": True})
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.first().name, 'John Doe')

    def test_register_student_view_with_invalid_data(self):
        self.form_data['student-roll_no'] = ''  # make the form data invalid
        url = reverse('register_student')
        response = self.client.post(url, data=self.form_data)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
            {"success": False, "errors": {"roll_no": ["This field is required."]}})
        self.assertEqual(Student.objects.count(), 0)
