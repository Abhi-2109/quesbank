# Generated by Django 2.2.1 on 2019-05-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190515_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquestion',
            name='question_level',
            field=models.IntegerField(default=0),
        ),
    ]