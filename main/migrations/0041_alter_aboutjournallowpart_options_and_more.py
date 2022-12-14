# Generated by Django 4.1.1 on 2022-09-17 11:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_aboutjournalcircletagline_delete_aboutjournaltagline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutjournallowpart',
            options={'verbose_name': 'О журнале', 'verbose_name_plural': 'О журнале'},
        ),
        migrations.AlterField(
            model_name='aboutjournallowpart',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='aboutjournallowpart',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='aboutjournallowpart',
            name='text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='aboutjournallowpart',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
