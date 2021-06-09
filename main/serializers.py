from rest_framework import serializers
from .models import *
from django.utils import timezone 
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username']


class MemberSerializer(serializers.Serializer):

	name = serializers.CharField(max_length=250,allow_null=True)
	PhotoLink = serializers.URLField(allow_null=True)
	PhotoFile = serializers.FileField(allow_null=True)
	TwitterLink = serializers.URLField(allow_null=True)
	GithubLink = serializers.URLField(allow_null=True)
	DribbleLink = serializers.URLField(allow_null=True)
	InstagramLink = serializers.URLField(allow_null=True)
	FacebookLink = serializers.URLField(allow_null=True)
	BehanceLink = serializers.URLField(allow_null=True)
	LinkedInLink = serializers.URLField(allow_null=True)
	team = serializers.CharField(max_length=200)
	batch = serializers.CharField(max_length=150,allow_null=True)
	designation = serializers.CharField(max_length=250,allow_null=True)
	is_Por_holder = serializers.BooleanField()

class BlogPostSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=300)
	author = UserSerializer(read_only=True)
	datePublished = serializers.DateTimeField(default=timezone.now)
	blogImageLink = serializers.URLField()
	read_time = serializers.CharField(max_length=100)
	about = serializers.CharField(style={'base_template': 'textarea.html'})
	blogLink = serializers.URLField()
	type_ = serializers.CharField(max_length=200,default='blog')

class Projects(serializers.Serializer):
	name = serializers.CharField(max_length=250)
	teamsInvolved = serializers.CharField(max_length=400) #Change to choices if needed
	date = serializers.DateTimeField()
	description = serializers.CharField(style={'base_template': 'textarea.html'})
	heroSectionImageLink = serializers.URLField()