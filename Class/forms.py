from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from .models import Class

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(Field('name', css_class='form-control mb-3'),
                                    Submit('submit', 'Create Class', css_class='btn btn-primary'), )
