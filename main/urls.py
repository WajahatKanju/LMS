from django.urls import path, include
from .views import HomeView
from .ajax_methods import  get_grades, register_student

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('get-grades/<uuid:school_id>/', get_grades),
    path('register-student/', register_student)

]

