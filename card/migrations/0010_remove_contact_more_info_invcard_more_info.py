# Generated by Django 4.0.3 on 2022-08-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0009_contact_more_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='more_info',
        ),
        migrations.AddField(
            model_name='invcard',
            name='more_info',
            field=models.CharField(default='', max_length=300),
        ),
    ]
