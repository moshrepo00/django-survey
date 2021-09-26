# Generated by Django 3.2.7 on 2021-09-25 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=200)),
                ('published', models.DateTimeField(verbose_name='date published')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.survey')),
            ],
        ),
    ]
