# Generated by Django 3.2.7 on 2021-09-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='published',
            field=models.DateTimeField(default=None),
        ),
    ]
