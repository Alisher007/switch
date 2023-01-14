from django.db import models
from django.urls import reverse

class Department(models.Model):

    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name



class Device(models.Model):

    name = models.CharField(max_length=500)
    department = models.ForeignKey(Department, related_name='devices', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('device:detail',args=[self.id])









