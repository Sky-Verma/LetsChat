# Generated by Django 3.1.1 on 2020-09-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='about',
            field=models.TextField(max_length=1000),
        ),
    ]
