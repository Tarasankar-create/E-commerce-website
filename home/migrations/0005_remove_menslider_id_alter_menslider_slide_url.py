# Generated by Django 5.1.6 on 2025-02-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_menslider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menslider',
            name='id',
        ),
        migrations.AlterField(
            model_name='menslider',
            name='slide_url',
            field=models.URLField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]
