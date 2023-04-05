from django.urls import path

from .views import SchoolView, SchoolDetailView, SchoolCreateView, SchoolUpdateView, SchoolDeleteView

app_name = 'school'

urlpatterns = [
    path('', SchoolView.as_view(), name='all'),
    path('school/create', SchoolCreateView.as_view(), name='create'),

    path('school/<uuid:pk>/', SchoolDetailView.as_view(), name='detail'),
    path('school/<uuid:pk>/update', SchoolUpdateView.as_view(), name='update'),
    path('school/<uuid:pk>/delete', SchoolDeleteView.as_view(), name='delete'),

    path('class/', SchoolView.as_view(), name='class'),
    path('class/create', SchoolCreateView.as_view(), name='class_create'),

    path('class/<uuid:pk>/', SchoolDetailView.as_view(), name='class_detail'),
    path('class/<uuid:pk>/update', SchoolUpdateView.as_view(), name='class_update'),
    path('class/<uuid:pk>/delete', SchoolDeleteView.as_view(), name='class_delete'),


]
