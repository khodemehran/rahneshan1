# Generated by Django 3.1.2 on 2020-12-27 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userdata', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='planetdata',
            name='Age_Numberic',
            field=models.IntegerField(default=1.0, help_text='اگر سن گیاه به صورت عددی باشد.'),
            preserve_default=False,
        ),
    ]
