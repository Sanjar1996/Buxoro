# Generated by Django 3.2.6 on 2021-08-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_newsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsitemodels',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]
