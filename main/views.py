from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def get_members(request,team):
	data = request.data
	try:
		members = Member.objects.filter(team=team)
		members_serializer = MemberSerializer(members,many=True)
		return Response(members_serializer.data,status=status.HTTP_200_OK)
	except:
		return Response({"error":"no such team"},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_member(request,pk):
	try:
		member = Member.objects.get(pk=pk)
		member_serializer = MemberSerializer(member)
		return Response(member_serializer.data,status=status.HTTP_200_OK)
	except:
		return Response({"error":"no such member"},status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def blog_detail(request, pk):
	data = request.data
	blog = BlogPost.objects.get(pk=pk)
	blog_serializer = BlogPostSerializer(blog)
	return Response(blog_serializer.data, status=status.HTTP_200_OK)
		


@api_view(['GET'])
def get_project(request, **kwargs):
	try:
		project = Project.objects.get(id = kwargs["pk"])
		project_serializer = ProjectsSerializer(project)
		return Response(project_serializer.data, status = status.HTTP_200_OK)
	except:
		return Response({"error" : "project not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_projects(request):
	try:
		projects = Project.objects.all()
		projects_serializer = ProjectsSerializer(projects,many=True)
		return Response(projects_serializer.data, status=status.HTTP_200_OK)
	except:
		return Response({"error":"projects not found"}, status=status.HTTP_404_NOT_FOUND)
