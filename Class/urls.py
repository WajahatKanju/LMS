from django.urls import path

from .views import (
    ClassView,
    ClassDetailView,
    ClassCreateView,
    ClassUpdateView,
    ClassDeleteView,
)

app_name = 'class'

urlpatterns = [
    path('', ClassView.as_view(), name='all'),
    path('class/create', ClassCreateView.as_view(), name='create'),

    path('class/<uuid:pk>/', ClassDetailView.as_view(), name='detail'),
    path('class/<uuid:pk>/update/', ClassUpdateView.as_view(), name='update'),
    path('class/<uuid:pk>/delete/', ClassDeleteView.as_view(), name='delete'),
]