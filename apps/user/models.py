from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
	WorkNumber = models.CharField(max_length=120, verbose_name='工号')
	Company = models.CharField(max_length=120, verbose_name='所属单位')

	class Meta:
		verbose_name = '用户个人信息'
		verbose_name_plural = verbose_name
		db_table = 'userprofile'


	def __str__(self):
		return self.username
