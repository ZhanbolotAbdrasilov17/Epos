# Generated by Django 4.1.1 on 2022-09-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_remove_maintagline_title_remove_maintagline_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintagline',
            name='title10',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название отправки сообщения'),
        ),
        migrations.AlterField(
            model_name='maintagline',
            name='title9',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название афиши'),
        ),
        migrations.AlterField(
            model_name='maintagline',
            name='title9_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название афиши'),
        ),
        migrations.AlterField(
            model_name='maintagline',
            name='title9_ky',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название афиши'),
        ),
        migrations.AlterField(
            model_name='maintagline',
            name='title9_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Название афиши'),
        ),
    ]