# Generated by Django 4.1.1 on 2022-09-20 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0071_delete_newstagline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Выпуски - Статьи', 'verbose_name_plural': 'Выпуски - Статьи'},
        ),
        migrations.AlterModelOptions(
            name='employees',
            options={'verbose_name': 'Мнение экспертов рынка', 'verbose_name_plural': 'Мнение экспертов рынка'},
        ),
        migrations.DeleteModel(
            name='Lizer',
        ),
        migrations.DeleteModel(
            name='LizerCategory',
        ),
    ]
