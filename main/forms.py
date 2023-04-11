from django import forms

from allauth.account.forms import SignupForm, LoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from school.models import Schools


class CustomSignupForm(SignupForm):
    # Define additional fields for the signup form
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    designation = forms.CharField(max_length=30, label='Designation', required=False)
    school = forms.ModelChoiceField(queryset=Schools.objects.all(), empty_label=None, label='School', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Use crispy_forms to generate a submit button and set form method
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign Up'))

        # Define the order and layout of the form fields
        self.helper.layout = Layout('username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                                    'designation', 'school')

    def save(self, request):
        # call the parent save method to create the user object
        user = super().save(request)

        # Save the additional fields to the user object
        user.designation = self.cleaned_data.get('designation')
        user.school = self.cleaned_data.get('school')
        user.active = True  # set active to True by default

        # Save the user object with the additional fields
        user.save()

        # Return the user object
        return user


class CustomLoginForm(LoginForm):
    # Define fields for the login form
    login = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Use crispy_forms to generate a submit button and set form method
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Log In'))

        # Define the order and layout of the form fields
        self.helper.layout = Layout('login', 'password')
