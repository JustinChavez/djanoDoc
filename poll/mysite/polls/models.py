from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.


#Makes the question here
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        #fixes bug to make sure publications that will be  published in the future
        #are not labeled as being published recently
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # text = models.TextField(null=True, blank=True)
    # author = models.ForeignKey(User, null=True )
    user = models.ForeignKey(to=User, related_name="use", blank=True, null=True)
    def __str__(self):
        return self.choice_text


# @python_2_unicode_compatible
#This is the model for the text change it to Roast becuase before it was named Post
#and i thought it will create errors
class Roast(models.Model):
    author = models.ForeignKey(User)
    # question_text = models.CharField(max_length=200)
    text = models.TextField()
    roast_title=models.CharField(max_length=200, default='Question')
    created_date = models.DateTimeField(
        default=timezone.now)

    # #Not complatiilbe with python 3 may be bad in the future
    # def __unicode__(self):
    #     return self.author + ' - ' + self.roast_title
# #
# class Vote(models.Model):
#     # class Meta:
#     #     unique_together = (('user', 'v[ote'),)
#     user = models.ForeignKey(User)
#     question = models.ForeignKey(Choice)




# User profile
class UserProfile(models.Model):
    user = models.OneToOneField(User)
