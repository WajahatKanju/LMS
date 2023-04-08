from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from school.models import Schools, Classes, SchoolClasses, ClassSubject
from main.models import Subject, Employee


class SchoolsModelTestCase(TestCase):
    def setUp(self):
        self.school = Schools.objects.create(name='ABC School', active=True)

    def test_get_form_url(self):
        self.assertEqual(self.school.get_form_url(), f'/school/{self.school.id}/update/')

    def test_get_delete_url(self):
        self.assertEqual(self.school.get_delete_url(), f'/school/{self.school.id}/delete/')

    def test_get_absolute_url(self):
        self.assertEqual(self.school.get_absolute_url(), f'/school/{self.school.id}/')

    def test_str(self):
        self.assertEqual(str(self.school), 'ABC School')


class ClassModelTestCase(TestCase):
    def setUp(self):
        self.classes = Classes.objects.create(name='Class 10', active=True)

    def test_str(self):
        self.assertEqual(str(self.classes), 'Class 10')


class SchoolClassModelTestCase(TestCase):
    def setUp(self):
        self.school = Schools.objects.create(name='ABC School', active=True)
        self.classes = Classes.objects.create(name='Class 10', active=True)
        self.school_classes = SchoolClasses.objects.create(school=self.school, classes=self.classes, pass_percentage=50,
                                                           active=True)

    def test_str(self):
        self.assertEqual(str(self.school_classes), 'Class 10 - ABC School')


class ClassSubjectModelTestCase(TestCase):
    def setUp(self):
        self.school = Schools.objects.create(name='ABC School', active=True)
        self.classes = Classes.objects.create(name='Class 10', active=True)
        self.school_classes = SchoolClasses.objects.create(school=self.school, classes=self.classes, pass_percentage=50,
                                                           active=True)
        self.subject = Subject.objects.create(name='Maths', active=True)
        self.user = User.objects.create_user(username='john.doe', email='john.doe@example.com', password='testpassword')
        self.employee = Employee.objects.create(user=self.user, designation='Teacher', school=self.school, active=True)
        self.class_subject = ClassSubject.objects.create(school_class=self.school_classes, subject=self.subject,
                                                         employee=self.employee, active=True)

    def test_str(self):
        self.assertEqual(str(self.class_subject), 'ABC School - Maths')


class SchoolsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.school = Schools.objects.create(name='Test School', active=True)
        self.classes = Classes.objects.create(name='Test Class', active=True)
        self.employee = Employee.objects.create(user=self.user, designation='Teacher', school=self.school)
        self.school_class = SchoolClasses.objects.create(classes=self.classes, school=self.school, active=True)

    def test_school_list_view(self):
        response = self.client.get(reverse('school:all'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'school/school_list.html')
        self.assertContains(response, self.school.name)

    def test_school_detail_view(self):
        url = reverse('school:detail', args=[self.school.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'school/school_detail.html')
        self.assertContains(response, self.school.name)

    def test_school_update_view(self):
        url = reverse('school:update', args=[self.school.id])
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'school/school_form.html')

    def test_school_delete_view(self):
        url = reverse('school:delete', args=[self.school.id])
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'school/school_delete.html')

    #
    def test_classes_list_view(self):
        response = self.client.get(reverse('school:class_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'school/class_list.html')
        self.assertContains(response,
                            self.classes.name)  #  # def test_classes_detail_view(self):  #     url = reverse('school:class_detail', args=[self.classes.id])  #     response = self.client.get(url)  #     self.assertEqual(response.status_code, 200)  #     self.assertTemplateUsed(response, 'school/class_detail.html')  #     self.assertContains(response, self.classes.name)  # #  # def test_classes_update_view(self):  #     url = reverse('school:class_update', args=[self.classes.id])  #     self.client.login(username='testuser', password='testpass')  #     response = self.client.get(url)  #     self.assertEqual(response.status_code, 200)  #     self.assertTemplateUsed(response, 'school/class_form.html')  #   # def test_classes_delete_view(self):  #     url = reverse('school:class_delete', args=[self.classes.id])  #     self.client.login(username='testuser', password='testpass')  #     response = self.client.get(url)  #     self.assertEqual(response.status_code, 200)  #     self.assertTemplateUsed(response, 'school/class_confirm_delete.html')  #   # def test_school_class_list_view(self):  #     response = self.client.get(reverse('school:school_class_list', args=[self.school.id]))  #     self.assertEqual(response.status_code, 200)  #     self.assertTemplateUsed(response, 'school/school_class_list.html')  #     self.assertContains(response, self.classes.name)
