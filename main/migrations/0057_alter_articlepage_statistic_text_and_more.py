# Generated by Django 4.1.1 on 2022-09-18 08:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0056_articlepage_statistic_pre_title_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='statistic_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст статистики'),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='statistic_text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст статистики'),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='statistic_text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст статистики'),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='statistic_text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст статистики'),
        ),
    ]
