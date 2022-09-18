# Generated by Django 4.1.1 on 2022-09-18 08:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_aboutjournallowpart_statistic_title_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesCircleTagline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст1')),
                ('title2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст2')),
                ('title3', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст3')),
                ('title4', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст4')),
                ('title5', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст5')),
                ('title6', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст6')),
                ('title7', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст7')),
            ],
            options={
                'verbose_name': 'Выпуска - планета',
                'verbose_name_plural': 'Выпуска - планета',
            },
        ),
        migrations.AlterField(
            model_name='articles',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='word',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='articlesarchive',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='articlesarchive',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='articlesarchive',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='articlesarchive',
            name='text_ky',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='articlesarchive',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='articlesarchive',
            name='word',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]