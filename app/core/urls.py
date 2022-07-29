

from django.urls import path, include
from .views import SettingsView, SettingsDetailView, SingletonSettingsView
urlpatterns = [
    path('settings/', SettingsView.as_view(), name='settings'),
    path('settings/<int:pk>/', SettingsDetailView.as_view(), name='settings-edit'),
    path('singleton/', SingletonSettingsView.as_view())
]
