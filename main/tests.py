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