from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class MyUser(AbstractUser):
	jifen = models.IntegerField('积分', default=0)

	class Meta:
		db_table = 'MyUser'

	def __str__(self):
		return self.username


class UserLogin(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=50)


class Article(models.Model):
	title=models.CharField("标题",max_length=50)
	authors=models.ManyToManyField(MyUser)
	created_date=models.DateField("创建日期",auto_now_add=True)
	modify_date=models.DateField("修改日期",auto_now=True)
	content=models.TextField()	
	is_show=models.BooleanField()

	class Meta:
		db_table="article"

	def __str__(self):
		return self.title



