from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Schools, Classes


class SchoolForm(forms.ModelForm):

    def clean(self):
        """
        Override the default clean method to check whether this School already exists
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
        fields = ['name', 'classes', ]

    classes = forms.ModelMultipleChoiceField(queryset=Classes.objects.all(), widget=forms.CheckboxSelectMultiple,
                                             required=False)

    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        submit = Submit('submit', 'Submit')
        self.helper.add_input(submit)
