# Generated by Django 5.1.6 on 2025-03-05 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_delete_login_signup_pin_alter_signup_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='mob',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='signup',
            name='pin',
            field=models.IntegerField(),
        ),
    ]
