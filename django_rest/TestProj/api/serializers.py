from rest_framework import serializers
from .models import Article, Release


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = '__all__'
