from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
import datetime
from datetime import datetime, timedelta

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    return now

@api_view(['GET'])
def to_do_week_view(request):
    """
    Returns all weekly tasks in database
    """
    tasks = ToDoWeek.objects.all()
    #put all tasks into variable tasks
    serializer = ViewtoDoWeekSerializer(tasks, many=True)
    #return serializer view
    return Response(serializer.data)

@api_view(['GET'])
def to_do_today_view(request):
    """
    Returns all current date tasks in database
    """
    entries = ToDoToday.objects.all()
    #put all tasks into variable tasks
    serializer = ViewtoDoTodaySerializer(entries, many=True)
    #return serializer view
    return Response(serializer.data)


@api_view(['GET'])
def notes_view(request):
    """
    Returns all current date tasks in database
    """
    entries = Note.objects.all()
    #put all tasks into variable tasks
    serializer = ViewNotesSerializer(entries, many=True)
    #return serializer view
    return Response(serializer.data)

