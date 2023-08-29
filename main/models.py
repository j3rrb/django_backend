from django.db import models
from uuid import uuid4
from datetime import timezone


class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField(null=False)

    def __str__(self) -> str:
        return f"{self.name}"


class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.TextField(null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Access(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.page}, data: {self.date.astimezone(timezone.utc).strftime('%d/%m/%Y, %H:%M:%S.%Z%z')}"
    

class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(null=False, max_length=50)
    age = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.name}"
    