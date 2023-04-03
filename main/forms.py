from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Settings


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
