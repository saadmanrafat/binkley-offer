# Generated by Django 3.1.2 on 2020-10-12 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0003_token_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_uid',
            field=models.TextField(unique=True),
        ),
    ]
