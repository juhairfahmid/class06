# Generated by Django 4.2.7 on 2023-11-24 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=50)),
                ('Student_Class', models.CharField(max_length=50)),
                ('Student_Roll', models.CharField(max_length=50)),
                ('Student_Bgroup', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_Name', models.CharField(max_length=50)),
                ('Teacher_Department', models.CharField(max_length=50)),
                ('Teacher_Resignation', models.CharField(max_length=50)),
                ('Teacher_Bgroup', models.CharField(max_length=50)),
            ],
        ),
    ]
