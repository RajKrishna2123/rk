# Generated by Django 2.2.7 on 2019-12-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=70)),
                ('Full_name', models.CharField(max_length=25)),
                ('problem_or_question', models.CharField(max_length=500)),
            ],
        ),
    ]
