from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    reminder_time = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        
        ordering = ('-due_date',)
        

    def __str__(self):
        return self.title
    
    