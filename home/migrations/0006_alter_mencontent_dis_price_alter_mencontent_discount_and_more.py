# Generated by Django 5.1.6 on 2025-02-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_menslider_id_alter_menslider_slide_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mencontent',
            name='dis_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mencontent',
            name='discount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mencontent',
            name='total',
            field=models.IntegerField(),
        ),
    ]
