# Generated by Django 2.2.1 on 2019-05-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190515_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectivequestion',
            name='question_html',
            field=models.CharField(default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='objectivequestion',
            name='solution_html',
            field=models.CharField(default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='subjectivequestion',
            name='question_html',
            field=models.CharField(default='', max_length=50000),
        ),
        migrations.AlterField(
            model_name='subjectivequestion',
            name='solution_html',
            field=models.CharField(default='', max_length=50000),
        ),
    ]
