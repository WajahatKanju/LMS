from django import forms

from allauth.account.forms import SignupForm, LoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

from school.models import Schools


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    designation = forms.CharField(max_length=30, label='Designation', required=False)
    school = forms.ModelChoiceField(queryset=Schools.objects.all(), empty_label=None, label='School', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign Up'))

        self.helper.layout = Layout('username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                                    'designation', 'school')

    def save(self, request):
        # call the parent save method
        user = super().save(request)

        # save the additional fields
        user.designation = self.cleaned_data.get('designation')
        user.school = self.cleaned_data.get('school')
        user.active = True  # set active to True by default

        user.save()

        return user


class CustomLoginForm(LoginForm):
    class CustomLoginForm(LoginForm):
        login = forms.CharField(label='Username')
        password = forms.CharField(widget=forms.PasswordInput(), label='Password')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Log In'))

            self.helper.layout = Layout('login', 'password')


        # class SettingsForm(forms.ModelForm):
#     class Meta:
#         model = Settings
#         fields = ['selected_school', 'selected_class', 'student_changes', 'batch_marks_changes',
#         'single_marks_changes', 'subject_changes', 'marks_lock_changes']
#
#     def __init__(self, *args, **kwargs):
#         super(SettingsForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(Row(Column('selected_school', css_class='form-group col-md-6'),
#                                         Column('selected_class', css_class='form-group col-md-6'), ),
#                                     Row(Column('student_changes', css_class='form-group col-md-6'),
#                                         Column('batch_marks_changes', css_class='form-group col-md-6'),
#                                         Column('single_marks_changes', css_class='form-group col-md-6'),
#                                         Column('subject_changes', css_class='form-group col-md-6'), ),
#                                     Row(Column('marks_lock_changes', css_class='form-group col-md-6'), ),
#                                     Submit('submit', 'Save', css_class='btn btn-primary'), )
