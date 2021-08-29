# Generated by Django 3.2.6 on 2021-08-29 13:09

from django.db import migrations, models
import xpress.models


class Migration(migrations.Migration):

    dependencies = [
        ('xpress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to=xpress.models.upload_to, verbose_name='Image'),
        ),
    ]