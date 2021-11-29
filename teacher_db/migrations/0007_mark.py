# Generated by Django 2.2.7 on 2019-12-20 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_db', '0006_auto_20191220_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('unit1', models.IntegerField()),
                ('unit2', models.IntegerField()),
                ('unit3', models.IntegerField()),
                ('final', models.IntegerField()),
                ('practicle', models.IntegerField()),
            ],
        ),
    ]
