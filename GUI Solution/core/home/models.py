from django.db import models
from django.contrib.auth.models import User


class Paragraph(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    paragraph_name = models.CharField(max_length=100)
    paragraph_description = models.TextField()
    paragraph_view_count = models.PositiveIntegerField(default=1)