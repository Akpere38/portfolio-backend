from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import Skill
from .serializers import SkillSerializer

class SkillListView(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
