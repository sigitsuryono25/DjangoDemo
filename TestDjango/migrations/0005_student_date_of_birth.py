# Generated by Django 2.1.3 on 2018-11-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestDjango', '0004_auto_20181106_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default='1990-01-01'),
        ),
    ]
