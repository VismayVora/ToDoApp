from django.db import models

# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length = 20)
	description = models.TextField()
	priority_no = models.IntegerField()
	status = models.BooleanField(default=False)
	duedate = models.DateTimeField()