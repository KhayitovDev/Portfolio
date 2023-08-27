# Generated by Django 4.1.5 on 2023-08-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_projectmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='file',
            field=models.FileField(default=1, upload_to='static/videos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
