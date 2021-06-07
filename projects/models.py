from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200)
    tag = models.TextField(default="")

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('toProgramDetail', kwargs={'pk': self.pk})

    def tags_as_list(self):
        return self.tag.split(',')
