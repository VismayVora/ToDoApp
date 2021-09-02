from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AppUser(AbstractUser):
	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'username'
	birth_date = models.DateField(null=True, blank=True)
	profile_pic = models.ImageField()
	#class Meta:
		#db_table = 'auth_user'

class Task_Category(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField(blank = True)
	def __str__(self):
		return self.title

class Task(models.Model):
	category = models.ForeignKey(Task_Category,null=True,on_delete = models.SET_NULL)
	title = models.CharField(max_length = 50)
	description = models.TextField(blank = True)
	priority_no = models.PositiveIntegerField(blank = True)
	status = models.BooleanField(default=False,blank = True)
	duedate = models.DateTimeField(blank = True)
	def __str__(self):
		return self.title