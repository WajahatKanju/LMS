import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import reverse


class Schools(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=30, unique=True)
    classes = models.ManyToManyField('Class.Class', through='SchoolClasses')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    def get_form_url(self):
        return reverse('school:update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('school:delete', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse('school:detail', args=[str(self.id)])

class SchoolClasses(models.Model):
    classes = models.ForeignKey('Class.Class', on_delete=models.CASCADE)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    pass_percentage = models.FloatField(default=33.3, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f'{self.classes.name} - {self.school.name}'


class ClassSubject(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    school_class = models.ForeignKey(SchoolClasses, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    subject = models.ForeignKey('main.Subject', on_delete=models.CASCADE)
    employee = models.ForeignKey('main.Employee', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school_class.school.name} - {self.subject.name}'
