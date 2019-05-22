# Generated by Django 2.2.1 on 2019-05-17 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hstu_school', '0002_stafflist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_time', models.TimeField(auto_now_add=True, verbose_name='Conversation Time')),
                ('event_date', models.DateField(auto_now_add=True, verbose_name='Conversation Date')),
                ('event_heading', models.CharField(max_length=150)),
                ('event_location', models.CharField(max_length=100)),
                ('event_details', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_time', models.TimeField(auto_now_add=True, verbose_name='Conversation Time')),
                ('news_date', models.DateField(auto_now_add=True, verbose_name='Conversation Date')),
                ('news_heading', models.CharField(max_length=150)),
                ('news_details', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_time', models.TimeField(auto_now_add=True, verbose_name='Conversation Time')),
                ('notice_date', models.DateField(auto_now_add=True, verbose_name='Conversation Date')),
                ('notice_heading', models.CharField(max_length=150)),
                ('notice_details', models.CharField(max_length=1000)),
            ],
        ),
    ]
