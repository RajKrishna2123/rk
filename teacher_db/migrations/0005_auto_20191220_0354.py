# Generated by Django 2.2.7 on 2019-12-19 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_db', '0004_marks_practicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='practicle',
            field=models.IntegerField(default='1'),
        ),
    ]
