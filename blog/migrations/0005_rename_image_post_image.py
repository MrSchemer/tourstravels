# Generated by Django 5.0.6 on 2024-05-29 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Image',
            new_name='image',
        ),
    ]
