# Generated by Django 3.1.3 on 2020-12-02 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201130_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_src',
            field=models.FileField(default='', upload_to='static/videos/'),
        ),
    ]
