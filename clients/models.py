from django.db import models
import uuid
import secrets

# Create your models here.

class APPClient(models.Model):
    client_name = models.CharField(max_length=24, primary_key=True)
    description = models.TextField()
    client_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    client_secret = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.client_secret:
            self.client_secret = secrets.token_urlsafe(128)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.client_name
