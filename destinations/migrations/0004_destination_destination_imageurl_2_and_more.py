# Generated by Django 4.1.12 on 2023-11-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0003_remove_destination_destination_searches_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='destination_imageURL_2',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='destination_imageURL_3',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='destination_imageURL_4',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='destination_imageURL_5',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='destination_imageURL_6',
            field=models.URLField(null=True),
        ),
    ]