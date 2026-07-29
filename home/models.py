from django.db import models
from django.contrib.auth.models import User

class LoginInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fails = models.PositiveSmallIntegerField(default=0)
    login_link = models.CharField(unique=True, blank=True, null=True, max_length=225)
    reset_link = models.CharField(unique=True, blank=True, null=True, max_length=225)

    def __str__(self):
        return self.user.username

class PhishingLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    flagged_input = models.TextField()
    risk_level = models.CharField(max_length=10)
    reason = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.risk_level} - {self.timestamp}"