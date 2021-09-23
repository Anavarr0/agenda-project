from django.urls import include, path

from . import views
from .views import *

urlpatterns = [
    path('weekly-tasks-list/', to_do_week_view),
    path('today-tasks-list/', to_do_today_view),
    path('notes-list/', notes_view),
]