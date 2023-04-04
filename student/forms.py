from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column, Layout
from betterforms.multiform import MultiModelForm

from .models import Student, StudentClass, StudentSchool


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_no', 'name', 'date_of_birth', 'admission_no', 'admission_date', 'student_cnic', 'father_cnic',
                  'mobile']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Row(Column('roll_no', css_class='form-group col-md-6'),
                                        Column('admission_no', css_class='form-group col-md-6'), ),
                                    Row(Column('date_of_birth', css_class='form-group col-md-6'),
                                        Column('admission_date', css_class='form-group col-md-6'), ),
                                    Row(Column('name', css_class='form-group col-md-3'),
                                        Column('student_cnic', css_class='form-group col-md-3'),
                                        Column('father_cnic', css_class='form-group col-md-3'),
                                        Column('mobile', css_class='form-group col-md-3'), ), )

        self.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['admission_date'].widget = forms.DateInput(attrs={'type': 'date'})


class StudentSchoolForm(forms.ModelForm):
    class Meta:
        model = StudentSchool
        fields = ['school']

    def __init__(self, *args, **kwargs):
        super(StudentSchoolForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Row(Column('school', css_class='form-group col-md-6'), ), )


class StudentClassForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = ['grade']

    def __init__(self, *args, **kwargs):
        super(StudentClassForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Row(Column('grade', css_class='form-group col-md-6'), ),
                                    Submit('submit', 'Add Student', css_class='btn btn-primary'))


class StudentRegistrationForm(MultiModelForm):
    form_classes = {'student': StudentForm, 'school': StudentSchoolForm, 'grade': StudentClassForm}
