from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")

    def __str__(self):
        return f'{self.id} | {self.title}'

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.TextField()
    qNumber = models.IntegerField()

    def __str__(self):
        return f'{self.qNumber} | {self.question} for survey "{self.survey.title}"'

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} | {self.author} answered {self.answer} for question: "{self.question.question}"'
