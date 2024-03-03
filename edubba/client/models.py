from django.contrib.auth.models import User
from django.db import models

from team.models import Team

# Create your models here.
class Client(models.Model):
    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    comment = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="clients", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return self.full_name