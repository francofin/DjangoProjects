from rest_framework import serializers
from .models import Journal



class JournalSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(max_length=300, read_only=True)
    url = serializers.URLField(max_length=300, allow_blank=True)
    user = serializers.StringRelatedField()
    class Meta:
        model = Journal
        fields = '__all__'
