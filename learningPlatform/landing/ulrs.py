from django.urls import path
from .views import Index, Review_List


urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('about/', Review_List.as_view(), name="about-us"),
]