# Generated by Django 3.0.6 on 2020-05-25 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('county', models.CharField(max_length=120)),
                ('ward', models.CharField(max_length=120)),
                ('village', models.CharField(max_length=120)),
                ('longitude', models.CharField(max_length=250)),
                ('latitude', models.CharField(max_length=250)),
                ('nearest_town', models.CharField(max_length=200)),
                ('national_id_no', models.IntegerField(blank=True)),
                ('passport_no', models.IntegerField(blank=True)),
                ('phone_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
