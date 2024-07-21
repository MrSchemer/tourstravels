# Generated by Django 5.0.6 on 2024-05-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_alter_package_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='published_date',
        ),
        migrations.AddField(
            model_name='package',
            name='difficulty',
            field=models.CharField(default='Easy', max_length=200),
        ),
        migrations.AddField(
            model_name='package',
            name='itinerary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='location',
            field=models.CharField(default='Nepal', max_length=200),
        ),
    ]