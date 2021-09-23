from django.db import models
import datetime
from datetime import date
from django.contrib.auth.models import User
#shows up every day on the agenda 
class ToDoWeek(models.Model):
    task = models.CharField(max_length=200)
    expiry = models.DateField()
    is_expired = models.BooleanField(default=False)
    def __str__(self):
        return f"task: {self.task} - expiry: {self.expiry} - is_expired: {self.is_expired}"

class ToDoToday(models.Model):
    currentDate= models.DateField(default=date.today())
    entry = models.CharField(max_length=500)
    def __str__(self):
        return f"date: {self.currentDate} - entry: {self.entry}"

class Note(models.Model):
    date = models.DateField(default=date.today())
    entry = models.CharField(max_length=500)
    def __str__(self):
        return f"date: {self.date} - entry: {self.entry}"
    
   
class Cal(models.Model):
    calories = models.IntegerField(default=0)
    def __str__(self):
        return f"calories: {self.calories}"

class Exercise(models.Model):
    date = models.DateField(default=date.today())
    entry = models.CharField(max_length=200)
    def __str__(self):
        return f"date: {self.date} - entry: {self.entry}"