# Generated by Django 3.1.2 on 2020-12-29 14:26

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('formola', '0006_remove_formola_relate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='content',
            field=djrichtextfield.models.RichTextField(null=True),
        ),
    ]