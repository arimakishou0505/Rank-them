# voting/models.py

from django.db import models

class Vote(models.Model):

    voted_at = models.DateTimeField(auto_now_add=True)


class Target(models.Model):
    name = models.CharField(max_length=100)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    group = models.CharField(max_length=100)  # グループを表すフィールド

    def total_votes(self):
        return self.up_votes - self.down_votes
    
class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name