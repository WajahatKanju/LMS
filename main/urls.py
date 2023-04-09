from django.urls import path, include
from .views import HomeView, get_grades

urlpatterns = [
    path('', HomeView.as_view(), name='home'),


    path('get-grades/<uuid:school_id>/', get_grades, name='get_grades')

]

