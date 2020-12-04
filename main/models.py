from django.db import models

# Create your models here.

class Video(models.Model):
    video_name = models.CharField(max_length = 30)
    video_img = models.ImageField(default = '' , upload_to='static/')
    video_src = models.FileField(default='', upload_to = 'static/videos/')

    def __str__(self):
        return self.video_name