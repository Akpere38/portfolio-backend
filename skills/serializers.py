# skills/serializers.py
from rest_framework import serializers
from .models import Skill

class SkillSerializer(serializers.ModelSerializer):
    icon = serializers.FileField(use_url=True)  
    # ensures full URL

    class Meta:
        model = Skill
        fields = '__all__'
