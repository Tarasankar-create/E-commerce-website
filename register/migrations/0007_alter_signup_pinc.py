# Generated by Django 5.1.6 on 2025-03-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_alter_signup_email_alter_signup_mob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='pinc',
            field=models.IntegerField(default=0),
        ),
    ]
