# Generated by Django 3.0 on 2021-04-08 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubservs', '0004_auto_20210408_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='blogs_suscribe',
            new_name='blogs_subcribe',
        ),
    ]