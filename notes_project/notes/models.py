import uuid
from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-edit_date']
