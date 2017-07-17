from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.title
