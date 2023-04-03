from django.urls import path
from .views import HomeView, SettingsView, SchoolView, SchoolDetailView, SchoolCreateView, SchoolUpdateView,\
    SchoolDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('settings/', SettingsView.as_view(), name='settings'),

    path('school/', SchoolView.as_view(), name='school'),
    path('school/create', SchoolCreateView.as_view(), name='school_create'),

    path('school/<uuid:pk>/', SchoolDetailView.as_view(), name='school_detail'),
    path('school/<uuid:pk>/update', SchoolUpdateView.as_view(), name='school_update'),
    path('school/<uuid:pk>/delete', SchoolDeleteView.as_view(), name='school_delete'),
]
