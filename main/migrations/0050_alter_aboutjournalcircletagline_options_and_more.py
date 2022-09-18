# Generated by Django 4.1.1 on 2022-09-17 16:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_alter_maintagline_title10_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutjournalcircletagline',
            options={'verbose_name': 'О журнале - планета', 'verbose_name_plural': 'О журнале - планета'},
        ),
        migrations.AddField(
            model_name='aboutjournallowpart',
            name='statistic_title',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Навзание поле статистики'),
        ),
        migrations.AlterField(
            model_name='aboutjournallowpart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='content', verbose_name='Картинка'),
        ),
    ]