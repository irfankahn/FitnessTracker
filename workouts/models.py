from django.db import models
from users.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # Duration in minutes
    calories = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.workout_type} by {self.user.username} on {self.date}"
