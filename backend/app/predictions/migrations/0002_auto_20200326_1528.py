# Generated by Django 3.0.2 on 2020-03-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='confirmed_images/'),
        ),
    ]