from django.urls import path

from .views import SchoolView, SchoolDetailView, SchoolCreateView, SchoolUpdateView, SchoolDeleteView

app_name = 'school'

urlpatterns = [
    path('', SchoolView.as_view(), name='all'),
    path('create', SchoolCreateView.as_view(), name='create'),

    path('<uuid:pk>/', SchoolDetailView.as_view(), name='detail'),
    path('<uuid:pk>/update/', SchoolUpdateView.as_view(), name='update'),
    path('<uuid:pk>/delete/', SchoolDeleteView.as_view(), name='delete'),

    path('class/', SchoolView.as_view(), name='class'),
    path('class/create', SchoolCreateView.as_view(), name='class_create'),

    path('class/<uuid:pk>/', SchoolDetailView.as_view(), name='class_detail'),
    path('class/<uuid:pk>/update/', SchoolUpdateView.as_view(), name='class_update'),
    path('class/<uuid:pk>/delete/', SchoolDeleteView.as_view(), name='class_delete'),


]
