from django.db import models

# Create your models here.
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Task(MPTTModel):
    STATUS_CHOICES = [
        ("RUN", "Running"),
        ("FIN", "Finished"),
        ("EXC", "Exception"),
        ("BAS", "Base"),
    ]

    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    body = models.CharField(max_length=500)

    # class MPTTMeta:
    #     order_insertion_by = ['name']
