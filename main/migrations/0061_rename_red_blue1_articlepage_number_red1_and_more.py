# Generated by Django 4.1.1 on 2022-09-18 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_alter_newscircletaglineone_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepage',
            old_name='red_blue1',
            new_name='number_red1',
        ),
        migrations.RenameField(
            model_name='articlepage',
            old_name='red_blue2',
            new_name='number_red2',
        ),
    ]