from django.contrib.auth.models import UserManager
from school.models import Schools


class CustomUserManager(UserManager):

    def create_user_from_form_data(self, form_data, password=None, **extra_fields):
        """
        Creates and saves a User with the given form data and password.
        """
        email = form_data['email']
        designation = form_data.get('designation', '')
        school_id = form_data.get('school', None)
        active = form_data.get('active', True)
        school = Schools.objects.get(id=school_id) if school_id else None
        user = self.model(email=email, designation=designation, school=school, active=active, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser_from_form_data(self, form_data, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given form data and password.
        """
        email = form_data['email']
        designation = form_data.get('designation', '')
        school_id = form_data.get('school', None)
        active = form_data.get('active', True)
        school = Schools.objects.get(id=school_id) if school_id else None
        user = self.create_superuser(email=email, password=password, designation=designation, school=school,
                                     active=active, **extra_fields)
        return user

    def create_staff_user_from_form_data(self, form_data, password=None, **extra_fields):
        """
        Creates and saves a staff user with the given form data and password.
        """
        email = form_data['email']
        designation = form_data.get('designation', '')
        school_id = form_data.get('school', None)
        active = form_data.get('active', True)
        school = Schools.objects.get(id=school_id) if school_id else None
        user = self.create_user(email=email, password=password, designation=designation, school=school, active=active,
                                is_staff=True, **extra_fields)
        return user

    def create_user(self, email, password=None, designation='', school=None, active=True, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        email = self.normalize_email(email)
        user = self.model(email=email, designation=designation, school=school, active=active, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, designation='', school=None, active=True, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        email = self.normalize_email(email)
        user = self.model(email=email, designation=designation, school=school, active=active, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff_user(self, email, password=None, designation='', school=None, active=True, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        email = self.normalize_email(email)
        user = self.model(email=email, designation=designation, school=school, active=active, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin_user(self, email, password=None, designation='', school=None, active=True, **extra_fields):
        """
        Creates and saves an admin user with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_admin', True)
        email = self.normalize_email(email)
        user = self.model(email=email, designation=designation, school=school, active=active, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
