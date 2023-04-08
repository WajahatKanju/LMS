from django.urls import path

from .views import SchoolView, SchoolDetailView, SchoolCreateView, SchoolUpdateView, SchoolDeleteView

app_name = 'school'

urlpatterns = [
    path('', SchoolView.as_view(), name='all'),
    path('create', SchoolCreateView.as_view(), name='create'),

    path('<uuid:pk>/', SchoolDetailView.as_view(), name='detail'),
    path('<uuid:pk>/update/', SchoolUpdateView.as_view(), name='update'),
    path('<uuid:pk>/delete/', SchoolDeleteView.as_view(), name='delete'),

]
