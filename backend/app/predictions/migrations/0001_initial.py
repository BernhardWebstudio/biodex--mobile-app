# Generated by Django 3.0.2 on 2020-03-31 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('image_url', models.URLField()),
                ('image_id', models.CharField(max_length=100)),
                ('family', models.CharField(max_length=100)),
                ('family_prob', models.FloatField(verbose_name='family probability')),
                ('subfamily', models.CharField(max_length=100)),
                ('subfamily_prob', models.FloatField(verbose_name='subfamily probability')),
                ('species', models.CharField(max_length=100)),
                ('species_prob', models.FloatField(verbose_name='species probability')),
                ('confirmed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='cases.Case')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
