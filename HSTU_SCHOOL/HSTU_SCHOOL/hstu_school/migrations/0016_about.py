# Generated by Django 2.2.1 on 2019-05-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hstu_school', '0015_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_date', models.DateField(auto_now_add=True, verbose_name='Conversation Date')),
                ('about_text', models.CharField(max_length=4000)),
            ],
        ),
    ]
