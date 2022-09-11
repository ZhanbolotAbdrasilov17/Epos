# Generated by Django 4.1 on 2022-09-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_employees_name_en_employees_name_ky_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название_видео')),
                ('file', models.FileField(upload_to='video', verbose_name='видео')),
                ('image', models.ImageField(blank=True, null=True, upload_to='content')),
            ],
            options={
                'verbose_name': 'Видео_Контент',
                'ordering': ['title'],
            },
        ),
    ]