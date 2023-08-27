from django.db import models

# Create your models here.

class AboutModel(models.Model):
    sub_title=models.CharField(max_length=250)
    start_date=models.CharField(max_length=250, blank=True)
    end_date=models.CharField(max_length=250, blank=True)
    title=models.CharField(max_length=250)
    description=models.TextField()

    def __str__(self):
        return self.sub_title
    
class ProjectModel(models.Model):
    image=models.ImageField(upload_to='static/images/')
    file=models.FileField(upload_to='static/videos/')
    title=models.CharField(max_length=250)
    description=models.TextField()

    def __str__(self):
        return self.title
    

    