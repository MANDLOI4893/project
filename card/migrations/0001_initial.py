# Generated by Django 4.0.3 on 2022-07-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='invcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default='', max_length=30, unique=True)),
                ('category', models.CharField(default='', max_length=50)),
                ('offer', models.CharField(blank=True, default='', max_length=20)),
                ('tag', models.CharField(blank=True, default='', max_length=10)),
                ('price', models.IntegerField(default='')),
                ('content', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(default='', upload_to='images/%y')),
                ('video', models.FileField(default='', upload_to='video/%y')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
