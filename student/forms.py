from django import forms
from django.core.exceptions import ValidationError

from .models import Student
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['roll_no', 'name', 'date_of_birth', 'admission_no', 'admission_date', 'student_cnic', 'father_cnic', 'mobile']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-8'
        self.helper.label_class = 'col-lg-2'

        self.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['admission_date'].widget = forms.DateInput(attrs={'type': 'date'})

        submit = Submit('Submit', 'Submit')
        self.helper.add_input(submit)
