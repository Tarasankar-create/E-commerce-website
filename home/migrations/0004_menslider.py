# Generated by Django 5.1.6 on 2025-02-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_mencontent_main_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='menSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_url', models.URLField(max_length=1000)),
            ],
        ),
    ]
