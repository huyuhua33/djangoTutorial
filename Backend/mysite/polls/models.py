import datetime

from django.db import models

from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    
    # Customization Function
    def was_published_recently(self):
        return self.pub_date >= timezone.now()
    
	# Std Function
    def __str__(self):
        returnTxT = self.question_text
        return returnTxT


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        returnTxT = self.choice_text
        return returnTxT


    
class Test(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        returnTxT = self.test_text
        return returnTxT