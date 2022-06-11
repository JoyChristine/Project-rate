from rest_framework import serializers
from .models import ProjectsAdded

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsAdded
        fields = ('name', 'context')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('author','email','bio','projects')