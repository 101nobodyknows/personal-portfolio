# Generated by Django 5.0.6 on 2024-10-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayokunnu', '0005_alter_image_gallery_main_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_desc', models.TextField()),
                ('my_img', models.ImageField(blank=True, upload_to='static/gallery_images')),
            ],
        ),
    ]