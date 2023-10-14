# Generated by Django 4.2.5 on 2023-10-12 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeDate', models.DateTimeField(auto_now_add=True)),
                ('likeUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likedBy', to=settings.AUTH_USER_MODEL)),
                ('likedPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='network.post')),
            ],
        ),
    ]
