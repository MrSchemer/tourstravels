# Generated by Django 5.0.6 on 2024-06-18 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='user_id',
        ),
    ]