from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import Project
from .serializers import ProjectSerializer

class ProjectListView(ListAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
