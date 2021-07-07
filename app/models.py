from django.db import models
from django.utils.datetime_safe import date


class ShowManager(models.Manager):
    def add_show_val(self, postData):
        errors ={}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show Network should be at least 3 characters"
        if len(postData['description']) < 10 :
            errors["description"] = "Show description should be at least 10 characters"
        if len(postData['release_date']) == '' :
            errors["release_date"] = "Show Release Date should be added"
        return errors


class Show(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=99)
    network = models.CharField(max_length=44)
    rel_date = models.DateField(default=date.today)
    desc = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = ShowManager()