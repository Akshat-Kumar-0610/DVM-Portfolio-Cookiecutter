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
	author = serializers.CharField(max_length=100)
	datePublished = serializers.DateTimeField(default=timezone.now)
	blogImageLink = serializers.URLField()
	read_time = serializers.CharField(max_length=100)
	about = serializers.CharField(style={'base_template': 'textarea.html'})
	blogLink = serializers.URLField(allow_null=True)
	artistName = serializers.CharField(max_length=250,allow_null=True)
	ArtLink = serializers.URLField(allow_null=True)
	DribbleLink = serializers.URLField(allow_null=True)
	BehanceLink = serializers.URLField(allow_null=True)
	InstagramLink = serializers.URLField(allow_null=True)
	LinkedInLink = serializers.URLField(allow_null=True)
	GithubLink = serializers.URLField(allow_null=True)
	otherLinks = serializers.CharField(style={'base_template': 'textarea.html'},allow_null=True)
	type_ = serializers.CharField(max_length=200,default='blog')


class ProjectsSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=250)
	teamsInvolved = serializers.CharField(max_length=400) #Change to choices if needed
	heroSectionImageLink = serializers.URLField()
	website_link = serializers.URLField()
	date = serializers.CharField(max_length=500)
	text_1 = serializers.CharField(style={'base_template': 'textarea.html'})
	text_2 = serializers.CharField(style={'base_template': 'textarea.html'})
	long_images_link = serializers.URLField()
	mockups_link = serializers.URLField()
	page_link = serializers.URLField()
	

	
