# Generated by Django 3.1.2 on 2021-01-09 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formola', '0014_auto_20210110_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formola',
            name='content',
            field=models.TextField(default='توضیحات اضافه:', help_text='توضیحات اضافه'),
        ),
    ]
