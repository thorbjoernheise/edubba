from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Lead(models.Model):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    CHOICES_PRIORITY = (
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High")
    )

    NEW = "new"
    CONTACTED = "contacted"
    WON = "won"
    LOST = "lost"

    CHOICES_STATUS = (
        (NEW, "New"),
        (CONTACTED, "Contacted"),
        (WON, "Won"),
        (LOST, "Lost")
    )

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    comment = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW)
    created_by = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return self.full_name