# Generated by Django 3.0.4 on 2020-05-26 18:28

from django.db import migrations, models
import farmers.models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0016_auto_20200526_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='cover',
            field=models.ImageField(blank=True, upload_to=farmers.models.upload_path),
        ),
    ]