# Generated by Django 2.2.7 on 2019-12-20 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_db', '0008_auto_20191220_0642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks',
            old_name='Prac',
            new_name='practicle',
        ),
    ]
