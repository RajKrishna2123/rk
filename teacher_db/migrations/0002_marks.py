# Generated by Django 2.2.7 on 2019-12-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('unit1', models.IntegerField()),
                ('unit2', models.IntegerField()),
                ('unit3', models.IntegerField()),
                ('final', models.IntegerField()),
            ],
        ),
    ]
