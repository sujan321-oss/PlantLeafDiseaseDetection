from django.db import models

# Create your models here.
class Tomato(models.Model):
    tomato=models.FileField(upload_to="tomato/",null=True)
    

class Potato(models.Model):
    potato=models.FileField(upload_to="potato/",null=True)
    

class Cotton(models.Model):
    cotton=models.FileField(upload_to="cotton/",null=True)