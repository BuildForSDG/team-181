# Generated by Django 3.0.4 on 2020-05-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0007_auto_20200526_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(related_name='products', to='farmers.Categories'),
        ),
    ]
