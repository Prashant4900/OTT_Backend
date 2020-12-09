from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('show/', views.ShowsLists.as_view()),
    path('', views.HomePage),
]

urlpatterns = format_suffix_patterns(urlpatterns)
