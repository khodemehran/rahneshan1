# Generated by Django 3.1.2 on 2021-01-09 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formola', '0015_auto_20210110_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formola',
            name='content',
            field=models.TextField(default='', help_text='توضیحات اضافه'),
        ),
    ]
