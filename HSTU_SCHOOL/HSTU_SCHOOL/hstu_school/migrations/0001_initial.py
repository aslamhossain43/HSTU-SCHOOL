# Generated by Django 2.2.1 on 2019-05-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
                ('photo_code', models.CharField(max_length=20)),
            ],
        ),
    ]
