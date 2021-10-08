from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article, Release
from .serializers import ArticleSerializer, ReleaseSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializers = ArticleSerializer(article, many=True)
        return Response(serializers.data)

    elif request.method == "POST":

        serializers = ArticleSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(author=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def release_list(request):
    if request.method == 'GET':
        article = Release.objects.all()
        serializers = ReleaseSerializer(article, many=True)
        return Response(serializers.data)

    elif request.method == "POST":

        serializers = Release(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def release_details(request, pk):
    try:
        release = Release.objects.get(pk=pk)

    except Release.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReleaseSerializer(release)
        # print(type(serializers))
        #article = release.author_set.all()
        #articleSerializer = ArticleSerializer(article)
        # print(serializer.data['city'])
        serializer.data['city'] = "None"
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ReleaseSerializer(release, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        Release.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
