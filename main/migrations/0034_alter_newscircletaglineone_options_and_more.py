# Generated by Django 4.1.1 on 2022-09-16 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_newscircletaglinetwo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newscircletaglineone',
            options={'verbose_name': 'Круг1 в выпусках', 'verbose_name_plural': 'Круг1 в выпусках'},
        ),
        migrations.AlterModelOptions(
            name='newscircletaglinetwo',
            options={'verbose_name': 'Круг2 в выпусках', 'verbose_name_plural': 'Круг2 в выпусках'},
        ),
    ]
