from django.db import models
from django.utils import timezone

class Time_tracker(models.Model):
    user_id = models.CharField(max_length = 64)
    project_id = models.CharField(max_length=64)
    tracking_date = models.DateTimeField(auto_now_add = True)
    task_description = models.CharField(max_length=64)
    num_of_hours_spent = models.IntegerField()

    def __str__(self):
        return str(self.tracking_date) + ' ' + str(self.user_id) + ' ' + str(self.project_id) + ' ' + str(self.num_of_hours_spent)