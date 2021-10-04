from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=40)
    role = models.CharField(max_length=40)
    status = models.BooleanField(null=False, default=True)
    salary_per_hour = models.FloatField()
    hours_per_week = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class Income(models.Model):
    amount = models.FloatField()
    description = models.TextField()
    stamp = models.DateTimeField(auto_now_add=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class Expense(models.Model):
    amount = models.FloatField()
    description = models.TextField()
    stamp = models.DateTimeField(auto_now_add=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class Message(models.Model):
    text = models.TextField(blank=False)
    stamp = models.DateTimeField(auto_now_add=True, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="chat_owner")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class Clients(models.Model):
    flow = models.BigIntegerField()
    stamp = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
