import datetime

from django import forms
from django.core.validators import MinValueValidator
from crispy_forms.layout import Submit, Row, Column, Layout
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from school.models import Schools, SchoolClasses
from .models import Student
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
    school = forms.ModelChoiceField(queryset=Schools.objects.all(), label='School', required=False)
    grade = forms.ModelChoiceField(queryset=SchoolClasses.objects.all(), label='Grade')
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date of birth',
                                    initial='1900-01-01', required=False)
    admission_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Admission date',
                                     initial=datetime.date.today, required=False)

    class Meta:
        model = Student
        fields = ['roll_no', 'name', 'father_name', 'gender', 'date_of_birth', 'admission_no', 'admission_date',
                  'student_cnic', 'father_cnic', 'mobile', 'grade', 'school']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['roll_no'].validators.append(MinValueValidator(1))
        self.fields['admission_no'].validators.append(MinValueValidator(1))

        self.helper.layout = Layout(
            Row(Column('roll_no', css_class='col-md-6'), Column('admission_no', css_class='col-md-6'), ),
            Row(Column('date_of_birth', css_class='col-md-6'), Column('admission_date', css_class='col-md-6'), ),
            Row(Column('name', css_class='col-md-3'), Column('father_name', css_class='col-md-3'),
                Column('student_cnic', css_class='col-md-3'), Column('father_cnic', css_class='col-md-3'), ),
            Row(Column('gender', css_class='col-md-3'), Column('mobile', css_class='col-md-3'),
                Column('school', css_class='col-md-3'), Column('grade', css_class='col-md-3'), ),
            FormActions(Submit('submit', 'Submit', css_class='btn-primary'), ), )

    def clean_grade(self):
        grade = self.cleaned_data['grade']
        print('clean_grade method called. grade:', grade)
        if grade not in SchoolClasses.objects.all():
            raise forms.ValidationError("Please select a valid grade.")
        return grade
