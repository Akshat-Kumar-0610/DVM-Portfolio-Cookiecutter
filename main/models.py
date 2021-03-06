from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Member(models.Model):
	teams = [('Backend','Backend'),
	('Frontend','Frontend'),
	('Video','Video'),
	('Design','Design'),
	('AppDev','AppDev')

	]
	name = models.CharField(max_length=250,null=True,blank=True)
	PhotoLink = models.URLField(null=True,blank=True)
	PhotoFile = models.FileField(null=True,blank=True)
	TwitterLink = models.URLField(null=True,blank=True)
	GithubLink = models.URLField(null=True,blank=True)
	DribbleLink = models.URLField(null=True,blank=True)
	InstagramLink = models.URLField(null=True,blank=True)
	FacebookLink = models.URLField(null=True,blank=True)
	BehanceLink = models.URLField(null=True,blank=True)
	LinkedInLink = models.URLField(null=True,blank=True)
	team = models.CharField(max_length=200,choices=teams)
	batch = models.CharField(max_length=150,null=True,blank=True)
	designation = models.CharField(max_length=250,null=True,blank=True)
	is_Por_holder = models.BooleanField()

	def __str__(self):
		return '{}----{}----{}'.format(self.name, self.team, self.pk)


class BlogPost(models.Model):
	types = [('blog','blog'),('artwork','artwork')]
	title = models.CharField(max_length=300)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	datePublished = models.DateTimeField(default=timezone.now)
	blogImageLink = models.URLField()
	read_time = models.CharField(max_length=100)
	about = models.TextField()
	blogLink = models.URLField()
	type_f = models.CharField(max_length=200,choices=types,default='blog')

	def __str__(self):
		return '{}----{}----{}'.format(self.title, self.type_f, self.pk)

class Projects(models.Model):
	name = models.CharField(max_length=250)
	teamsInvolved = models.CharField(max_length=400) #Change to choices if needed
	date = models.DateTimeField()
	description = models.TextField()
	heroSectionImageLink = models.URLField()

	def __str__(self):
		return '{}----{}----{}'.format(self.name, self.teamsInvolved, self.pk)

