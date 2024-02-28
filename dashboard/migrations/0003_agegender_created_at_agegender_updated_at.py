# Generated by Django 5.0.2 on 2024-02-28 19:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_add_camera_foreignkey_for_AgeGender_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='agegender',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agegender',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]