from rest_framework import serializers, generics
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import settings

class ViewtoDoWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoWeek
        fields = ('task', 'expiry', 'is_expired')

class ViewtoDoTodaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoToday
        fields = ('currentDate', 'entry')

class ViewNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('date', 'entry')
