from rest_framework import serializers
from .models import Job, CandidatesApplied

class JobSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    user = serializers.StringRelatedField()
    class Meta:
        model=Job
        fields = '__all__'


class CandidateAppliedSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    job = JobSerializer()
    class Meta:
        model=CandidatesApplied
        fields = ('user', 'resume', 'applied_at', 'job')
