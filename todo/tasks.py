from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from todo.models import Task

@shared_task
def send_task_reminder(task_id):
    try:
        task = Task.objects.get(id=task_id)
        if not task.is_completed and task.reminder_time > timezone.now():
            # Send reminder logic (e.g., email, notification)
            print(f"Reminder for task '{task.title}'")
    except Task.DoesNotExist:
        pass