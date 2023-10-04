# Generated by Django 3.2.7 on 2023-04-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveytaker', '0011_response_camera_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='calibration_acc',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='screen_size',
            field=models.CharField(max_length=5000000, null=True),
        ),
    ]
