from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(max_length=300, read_only=True)
    url = serializers.URLField(max_length=300, allow_blank=True)
    url2 = serializers.URLField(max_length=300, allow_blank=True)
    url3 = serializers.URLField(max_length=300, allow_blank=True)
    picture6 = serializers.ImageField()
    picture1 = serializers.ImageField()
    picture2 = serializers.ImageField()
    picture3 = serializers.ImageField()
    picture4 = serializers.ImageField()
    picture5 = serializers.ImageField()
    video = serializers.FileField()
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = '__all__'






    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)


    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.description1 = validated_data.get('description1', instance.description1)
    #     instance.description2 = validated_data.get('description2', instance.description2)
    #     instance.slug = validated_data.get('slug', instance.slug)
    #     instance.url = validated_data.get('url', instance.url)
    #     instance.url2 = validated_data.get('url2', instance.url2)
    #     instance.url3 = validated_data.get('url3', instance.url3)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance