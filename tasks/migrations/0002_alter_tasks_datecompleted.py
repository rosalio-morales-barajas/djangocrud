# Generated by Django 5.1.2 on 2024-10-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='dateCompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
