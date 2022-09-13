# Generated by Django 4.1 on 2022-09-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_videocontent_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст')),
                ('title_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст')),
                ('title_ky', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст')),
                ('title_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]