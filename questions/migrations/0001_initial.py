# Generated by Django 3.1.3 on 2021-11-01 23:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_DB',
            fields=[
                ('qno', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100)),
                ('optionA', models.CharField(max_length=100)),
                ('optionB', models.CharField(max_length=100)),
                ('optionC', models.CharField(max_length=100)),
                ('optionD', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=200)),
                ('max_marks', models.IntegerField(default=0)),
                ('professor', models.ForeignKey(limit_choices_to={'groups__name': 'Professor'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question_Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qPaperTitle', models.CharField(max_length=100)),
                ('professor', models.ForeignKey(limit_choices_to={'groups__name': 'Professor'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(to='questions.Question_DB')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('total_marks', models.IntegerField()),
                ('start_time', models.DateTimeField(default=datetime.datetime(2021, 11, 1, 23, 27, 43, 902444, tzinfo=utc))),
                ('end_time', models.DateTimeField(default=datetime.datetime(2021, 11, 1, 23, 27, 43, 902476, tzinfo=utc))),
                ('professor', models.ForeignKey(limit_choices_to={'groups__name': 'Professor'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='questions.question_paper')),
            ],
        ),
    ]
