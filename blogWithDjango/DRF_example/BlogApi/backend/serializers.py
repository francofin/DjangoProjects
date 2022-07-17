from rest_framework import serializers
from .models import Article

# class ArticleSerializer(serializers.Serializer):
#     # Need to specify all the fields ourselves with serializers.Serializer.
#     # needs the create and update methods.
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     slug = serializers.SlugField(max_length=200)
#     published = serializers.DateTimeField(read_only=True)



#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.published = validated_data.get('published', instance.published)
#         instance.save()
#         return instance


class ArticleSerializer(serializers.ModelSerializer):
    # Need to specify all the fields ourselves with serializers.Serializer.
    # needs the create and update methods.
    # Model serializer, validates the model and includes default implementation of update and create, where we would need to specify in a regular serializer
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()
    class Meta:
        model=Article
        fields = '__all__' #This serializes all fields rather than a list of individual fields.

 