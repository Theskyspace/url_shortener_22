# Generated by Django 4.0.5 on 2022-12-23 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls',
            old_name='Uuid',
            new_name='myid',
        ),
    ]
