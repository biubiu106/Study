# Generated by Django 2.2.7 on 2019-12-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_type',
            field=models.IntegerField(default=1),
        ),
    ]
