from django.urls import path, include
from .views import HomeView, SettingsView, get_grades

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('accounts/', include('allauth.urls')),

    path('get-grades/<uuid:school_id>/', get_grades, name='get_grades')

]

