# Generated by Django 5.1.4 on 2025-01-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayokunnu', '0013_imagegallery_rename_new_message_newmessage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='phone',
            field=models.TextField(blank=True, default='07044584688'),
        ),
    ]