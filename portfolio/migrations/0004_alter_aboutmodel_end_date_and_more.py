# Generated by Django 4.2.4 on 2023-08-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_projectmodel_file_alter_projectmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='end_date',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='start_date',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
