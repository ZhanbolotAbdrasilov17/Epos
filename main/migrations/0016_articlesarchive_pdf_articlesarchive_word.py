# Generated by Django 4.1 on 2022-09-11 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_firsttagline_articles_pdf_articles_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesarchive',
            name='pdf',
            field=models.FileField(default=11, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlesarchive',
            name='word',
            field=models.FileField(default=112, upload_to=''),
            preserve_default=False,
        ),
    ]
