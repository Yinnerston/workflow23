from django.db import models

# Create your models here.
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator


class Task(MPTTModel):
    STATUS_CHOICES = [
        ("RUN", "Running"),
        ("FIN", "Finished"),
        ("EXC", "Exception"),
        ("BAS", "Base"),
    ]
    COORD_MIN = -10000
    COORD_MAX = 10000

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
    x = models.BigIntegerField(
        default=0,
        validators=[MinValueValidator(COORD_MIN), MaxValueValidator(COORD_MAX)],
    )
    y = models.BigIntegerField(
        default=0,
        validators=[MinValueValidator(COORD_MIN), MaxValueValidator(COORD_MAX)],
    )

    class MPTTMeta:
        order_insertion_by = ["name"]
