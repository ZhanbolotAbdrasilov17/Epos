# Generated by Django 4.1.1 on 2022-09-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_lizercategory_lizer_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCircleTaglineOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Слово')),
            ],
            options={
                'verbose_name': 'Круг1',
                'verbose_name_plural': 'Круг1',
            },
        ),
    ]
