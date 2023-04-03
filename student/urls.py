from django.urls import path
from .views import StudentView, StudentCreateView, StudentUpdateView, StudentDetailView, StudentDeleteView

app_name = 'student'

urlpatterns = [
    path('', StudentView.as_view(), name='all'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='delete'),
]
