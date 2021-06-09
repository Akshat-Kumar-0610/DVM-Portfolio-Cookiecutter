from rest_framework import serializers
from .models import *
from django.utils import timezone 
from django.contrib.auth import User 

class UserSerializer(serializers.ModelSerializer):
	class Meta:
	model = User
	fields = ['id','username']


class MemberSerializer(serializers.Serializer):

	name = serializers.CharField(max_length=250,allow_blank=True)
	PhotoLink = serializers.URLField(allow_blank=True)
	PhotoFile = serializers.FileField(null=True,allow_blank=True)
	TwitterLink = serializers.URLField(null=True,allow_blank=True)
	GithubLink = serializers.URLField(null=True,allow_blank=True)
	DribbleLink = serializers.URLField(null=True,allow_blank=True)
	InstagramLink = serializers.URLField(null=True,allow_blank=True)
	FacebookLink = serializers.URLField(null=True,allow_blank=True)
	BehanceLink = serializers.URLField(null=True,allow_blank=True)
	LinkedInLink = serializers.URLField(null=True,allow_blank=True)
	team = serializers.CharField(max_length=200)
	batch = serializers.CharField(max_length=150,allow_blank=True)
	designation = serializers.CharField(max_length=250,allow_blank=True)
	is_Por_holder = serializers.BooleanField()

class BlogPostSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=300)
	author = UserSerializer(read_only=True)
	datePublished = serializers.DateTimeField(default=timezone.now)
	blogImageLink = serializers.URLField()
	read_time = serializers.CharField(max_length=100)
	about = serializers.TextField()
	blogLink = serializers.URLField()
	type_ = serializers.CharField(max_length=200,default='blog')

class Projects(serializers.Serializer):
	name = serializers.CharField(max_length=250)
	teamsInvolved = serializers.CharField(max_length=400) #Change to choices if needed
	date = serializers.DateTimeField()
	description = serializers.TextField()
	heroSectionImageLink = serializers.URLField()