from django.db import models



class Survey(models.Model):
    survey_title = models.CharField(max_length=200)
    published= models.DateTimeField(default=None)
    def __str__(self):
        return self.survey_title

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=200)
    published = models.DateTimeField('date published')


