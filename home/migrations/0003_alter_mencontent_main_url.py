# Generated by Django 5.1.6 on 2025-02-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_mencontent_dis_price_alter_mencontent_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mencontent',
            name='main_url',
            field=models.URLField(max_length=1000),
        ),
    ]
