from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Feedback(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    subject = models.CharField(
        max_length=100,
    )
    message = models.TextField(
        max_length=5000,
    )
    email = models.EmailField(
        null=True,
        blank=True,
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True
    )
    file = models.FileField(
        upload_to='media/',
        blank=True,
        null=True
    )
    time_created = models.DateTimeField(
        'Время создания',
        auto_now_add=True,
        blank=True,
        null=True
    )
    is_read = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'{self.user} ({self.time_created})'

