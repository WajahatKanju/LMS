from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.exceptions import ValidationError

from .models import Settings, Schools, Classes


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['selected_school', 'selected_class', 'student_changes', 'batch_marks_changes', 'single_marks_changes',
                  'subject_changes', 'marks_lock_changes']

    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(Row(Column('selected_school', css_class='form-group col-md-6'),
            Column('selected_class', css_class='form-group col-md-6'), ),
            Row(Column('student_changes', css_class='form-group col-md-6'),
                Column('batch_marks_changes', css_class='form-group col-md-6'),
                Column('single_marks_changes', css_class='form-group col-md-6'),
                Column('subject_changes', css_class='form-group col-md-6'), ),
            Row(Column('marks_lock_changes', css_class='form-group col-md-6'), ),
            Submit('submit', 'Save', css_class='btn btn-primary'), )


class SchoolForm(forms.ModelForm):

    def clean(self):
        """
        Override the default clean method to check whether this course has
        been already inputted.
        """
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')

        matching_schools = Schools.objects.filter(name=name)
        if self.instance:
            matching_schools = matching_schools.exclude(pk=self.instance.pk)
        if matching_schools.exists():
            msg = u"School: %s  already exist." % name
            raise ValidationError(msg)
        else:
            return self.cleaned_data

    class Meta:
        model = Schools
        fields = ['name', 'classes']

    classes = forms.ModelMultipleChoiceField(queryset=Classes.objects.all(), widget=forms.CheckboxSelectMultiple,
                                             required=False)

    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        submit = Submit('submit', 'Submit')
        self.helper.add_input(submit)
