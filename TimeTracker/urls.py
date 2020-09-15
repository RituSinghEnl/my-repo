from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from rest_framework import renderers
from TimeTracker import views
from rest_framework.routers import DefaultRouter
from TimeTracker.views import User_viewset

router = DefaultRouter()
router.register(r'time_tracker', views.User_viewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]