# Generated by Django 2.2.1 on 2019-05-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190515_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectivequestion',
            name='question_html',
            field=models.CharField(default='', max_length=30000),
        ),
        migrations.AlterField(
            model_name='objectivequestion',
            name='solution_html',
            field=models.CharField(default='', max_length=30000),
        ),
        migrations.AlterField(
            model_name='subjectivequestion',
            name='question_html',
            field=models.CharField(default='', max_length=30000),
        ),
        migrations.AlterField(
            model_name='subjectivequestion',
            name='solution_html',
            field=models.CharField(default='', max_length=30000),
        ),
    ]