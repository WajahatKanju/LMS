from django.urls import path, include
from .views import HomeView, SettingsView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('accounts/', include('allauth.urls')),


]
