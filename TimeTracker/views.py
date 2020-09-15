from rest_framework import viewsets 
from TimeTracker.serializers import User_serializer
from TimeTracker.models import Time_tracker
from django.contrib.auth.models import User
from rest_framework import permissions



class User_viewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Time_tracker.objects.all()
    serializer_class = User_serializer
    permission_classes = [permissions.IsAuthenticated]

