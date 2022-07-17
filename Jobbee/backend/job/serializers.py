from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    user = serializers.StringRelatedField()
    class Meta:
        model=Job
        fields = '__all__'
