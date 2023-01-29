from django.db import models

class IgHashtag(models.Model):
    hashtag_id = models.BigIntegerField()
    hashtag_word = models.CharField(max_length=100)
