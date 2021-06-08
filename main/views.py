from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import *

# Create your views here.
@api_view(['GET'])
def get_members(request,team):
	data = request.data
	try:
		members = Member.objects.filter(team=team)
		return Response(members.to_dict(),status=status.HTTP_200_OK)
	except:
		return Response({"error":"no such team"},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_member(request,pk):
	try:
		member = Member.objects.get(pk=pk)
		return Response(member.to_dict(),status=status.HTTP_200_OK)
	except:
		return Response({"error":"no such member"},status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_member(request):
	data = request.data
	name = data["name"]
	PhotoLink = data["PhotoLink"]
	TwitterLink = data["TwitterLink"]
	GithubLink = data["GithubLink"]
	DribbleLink = data["DribbleLink"]
	InstagramLink = data["InstagramLink"]
	FacebookLink = data["FacebookLink"]
	BehanceLink = data["BehanceLink"]
	LinkedInLink = data["LinkedInLink"]
	team = data["team"]
	batch = data["batch"]
	designation = data["designation"]
	is_Por_holder = data["is_Por_holder"]
	try:
		member=Member.objects.create(
			name=name,
			PhotoLink=PhotoLink,
			TwitterLink=TwitterLink,
			GithubLink=GithubLink,
			DribbleLink=DribbleLink,
			InstagramLink=InstagramLink,
			FacebookLink=FacebookLink,
			BehanceLink=BehanceLink,
			LinkedInLink=LinkedInLink,
			team=team,
			batch=batch,
			designation=designation,
			is_Por_holder=is_Por_holder,
			)
		member.save()
		return Response(status=status.HTTP_201_CREATED)
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_member(request,pk):
	try:
		member = Member.objects.get(pk=pk)
		member.delete()
		return Response(status=status.HTTP_200_OK)
	except:
		return Response({"error":"no such member"},status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_member(request,pk):
	try:
		member = Member.objects.get(pk=pk)
		data = request.data
		member.name = data["name"]
		member.PhotoLink = data["PhotoLink"]
		member.TwitterLink = data["TwitterLink"]
		member.GithubLink = data["GithubLink"]
		member.DribbleLink = data["DribbleLink"]
		member.InstagramLink = data["InstagramLink"]
		member.FacebookLink = data["FacebookLink"]
		member.BehanceLink = data["BehanceLink"]
		member.LinkedInLink = data["LinkedInLink"]
		member.team = data["team"]
		member.batch = data["batch"]
		member.designation = data["designation"]
		is_Por_holder = data["is_Por_holder"]
		member.save()
		return Response(member.to_dict(),status=status.HTTP_200_OK)
	except:
		return Response({"error":"no such member"},status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def new_blog(request):
	data = request.data
	title = data['title']
	author = data['author']
	datePublished = data['datePublished']
	blogImageLink = data['blogImageLink']
	read_time = data['read_time']
	about = data['about']
	blogLink = data['blogLink']
	try:
		blog = BlogPost(title=title, author=author, datePublished=datePublished, blogImageLink=blogImageLink, read_time=read_time, about=about, blogLink=blogLink)
		blog.save()
	except:
		return Response({"error":"not able to create blog"},status=status.HTTP_400_BAD_REQUEST)	
	return Response(blog.to_dict(), status=status.HTTP_201_CREATED)

@api_view(['GET'])
def blog_detail(request, **kwargs):
	data = request.data
	blog = BlogPost.objects.filter(id=kwargs['pk'])
	if blog.exists():
		return Response(blog.to_dict(), status=status.HTTP_200_OK)
	else:
		return Response({"error":"blog not found"},status=status.HTTP_404_NOT_FOUND)	

@api_view(['DELETE'])
def blog_delete(request, **kwargs):
	data = request.data
	try:
		blog = BlogPost.objects.filter(id=kwargs['pk'])
		blog.delete()
	except:
		return Response({"error":"not able to delete blog"},status=status.HTTP_400_BAD_REQUEST)	
	return Response(status=status.HTTP_200_OK)

@api_view(['PUT'])
def blog_update(request, **kwargs):
	data = request.data
	blog = BlogPost.objects.filter(id=kwargs['pk'])
	if blog.exists():

		blog.title = data['title']
		blog.author = data['author']
		blog.datePublished = data['datePublished']
		blog.blogImageLink = data['blogImageLink']
		blog.read_time = data['read_time']
		blog.about = data['about']
		blog.blogLink = data['blogLink']
		blog.save()
	else:
		return Response({"error":"not able to update blog"},status=status.HTTP_400_BAD_REQUEST)	
	return Response(blog.to_dict(), status=status.HTTP_201_CREATED)

