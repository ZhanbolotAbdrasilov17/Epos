# Generated by Django 4.1 on 2022-09-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_rename_videocontent_content_alter_content_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='link',
        ),
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название'),
        ),
    ]
