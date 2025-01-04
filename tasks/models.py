from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    completed = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True) 
    due_date = models.DateTimeField(null=True, blank=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return self.title
