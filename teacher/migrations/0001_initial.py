# Generated by Django 2.2.7 on 2019-12-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='marks',
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
        migrations.CreateModel(
            name='teacher_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_Name', models.CharField(max_length=50)),
                ('Current_class', models.CharField(max_length=8)),
                ('SCHOOL_name', models.CharField(max_length=70)),
                ('Subject', models.CharField(max_length=50)),
            ],
        ),
    ]