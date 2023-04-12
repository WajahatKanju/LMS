from django.http import JsonResponse
from school.models import SchoolClasses
from django.views.decorators.csrf import csrf_exempt
from student.forms import StudentForm


def get_grades(request, school_id):
    grades = SchoolClasses.objects.filter(school_id=school_id).values('id', 'classes', 'classes__name', 'school__name')
    grades_dict = {
        grade['id']: {'id': grade['classes'], 'name': (grade['classes__name'] + " - " + grade['school__name'])} for
        grade in grades}
    print(f'grades dict {grades_dict}')
    return JsonResponse(grades_dict)





@csrf_exempt
def register_student(request):
    if request.method == 'POST':
        student_roll_no = request.POST.get('student-roll_no')
        student_admission_no = request.POST.get('student-admission_no')
        student_date_of_birth = request.POST.get('student-date_of_birth')
        student_admission_date = request.POST.get('student-admission_date')
        student_name = request.POST.get('student-name')
        student_father_name = request.POST.get('student-father_name')
        student_student_cnic = request.POST.get('student-student_cnic')
        student_father_cnic = request.POST.get('student-father_cnic')
        student_gender = request.POST.get('student-gender')
        student_mobile = request.POST.get('student-mobile')
        student_school = request.POST.get('student-school')
        student_class = request.POST.get('student-grade')

        data = {
            'roll_no': student_roll_no,
            'admission_no': student_admission_no,
            'date_of_birth': student_date_of_birth,
            'admission_date': student_admission_date,
            'name': student_name,
            'father_name': student_father_name,
            'student_cnic': student_student_cnic,
            'father_cnic': student_father_cnic,
            'gender': student_gender,
            'mobile': student_mobile,
            'school': student_school,
            'grade': student_class,
        }

        # Create a new instance of the StudentForm and pass the submitted data to it
        form = StudentForm(data=data)

        # If the form is valid, save the data to the database and return a success response
        # If the form is not valid, return an error response with an error message
        if form.is_valid():
            # Save the form data to the database here
            form.save()
            # Return a success response with a JSON payload
            return JsonResponse({'success': True})
        else:
            # Get all form errors as a dict and send them in the response
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        # Handle GET requests to the form submission URL
        return JsonResponse({'success': False, 'error_message': 'Invalid request method.'})