# Generated by Django 5.0.3 on 2024-04-02 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0003_xpathimporter_date_format_xpathimporter_time_format_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evententry',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='evententry',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='evententry',
            name='tagline',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
