# Generated by Django 4.2.1 on 2023-05-15 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cotton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cotton', models.FileField(upload_to='cotton/')),
            ],
        ),
        migrations.CreateModel(
            name='Potato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('potato', models.FileField(upload_to='potato/')),
            ],
        ),
        migrations.CreateModel(
            name='Tomato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tomato', models.FileField(upload_to='tomato/')),
            ],
        ),
    ]
