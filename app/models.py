from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200, null=False)
    identityNumber = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employee_edit', kwargs={'pk': self.pk})