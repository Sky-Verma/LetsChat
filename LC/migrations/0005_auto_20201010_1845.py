# Generated by Django 3.1.2 on 2020-10-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LC', '0004_auto_20201007_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='user_info',
            name='profile_pic',
            field=models.ImageField(blank=True, default='defaultUser.png', null=True, upload_to=''),
        ),
    ]
