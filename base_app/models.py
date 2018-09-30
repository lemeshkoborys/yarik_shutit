from django.db import models


class Joke(models.Model):
    
    class Meta:
        db_table = 'jokes'

    title = models.CharField(
        max_length=120
    )

    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
