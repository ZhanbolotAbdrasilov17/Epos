# Generated by Django 4.1.1 on 2022-09-20 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0069_alter_bluetagline_options_alter_redtagline_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArticlesTagline',
        ),
        migrations.AlterModelOptions(
            name='maintagline',
            options={'verbose_name': 'Главная - Контент', 'verbose_name_plural': 'Главная - Контент'},
        ),
        migrations.AlterModelOptions(
            name='videocontent',
            options={'verbose_name': 'Новости - Видео', 'verbose_name_plural': 'Новости - Видео'},
        ),
    ]
