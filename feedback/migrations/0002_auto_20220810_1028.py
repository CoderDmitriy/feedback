# Generated by Django 3.2.15 on 2022-08-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
