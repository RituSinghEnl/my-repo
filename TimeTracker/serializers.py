from rest_framework import serializers
from TimeTracker.models import Time_tracker
from django.contrib.auth.models import User

class User_serializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:  
        model = Time_tracker
        fields = ['user_id' , 'project_id' , 'tracking_date' , 'task_description' , 'num_of_hours_spent']