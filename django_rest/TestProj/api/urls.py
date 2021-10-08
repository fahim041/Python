from django.urls import path
from .views import article_details, article_list, release_list, release_details

urlpatterns = [
    path('article/', article_list),
    path('article/<str:pk>', article_details),
    path('release/', release_list),
    path('release/<int:pk>', release_details)
]
