# Generated by Django 4.1.3 on 2022-11-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postit_api', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
    ]
