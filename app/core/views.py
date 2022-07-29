from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework import permissions

# Create your views here.
from core.models import Settings, SingletonSettings


class SettingsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = (
            'setting1',
            'setting2',
            'setting3',
        )


class SingletonSettingsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = SingletonSettings
        fields = (
            'setting1',
            'setting2',
            'setting3',
        )


class SettingsView(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = SettingsSerialiser
    queryset = Settings.objects.all()


class SettingsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SettingsSerialiser
    queryset = Settings.objects.all()


class SingletonSettingsView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = SingletonSettingsSerialiser
    queryset = SingletonSettings.objects.all()

    def get_object(self):
        obj = SingletonSettings.get_solo()
        self.check_object_permissions(self.request, obj)
        return obj
