# Generated by Django 2.2.1 on 2019-05-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hstu_school', '0007_auto_20190517_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_details',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_details',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_details',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
    ]