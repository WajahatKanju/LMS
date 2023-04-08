import uuid
from django.db import models


class Class(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'
