# Generated by Django 3.1.2 on 2021-01-04 15:36

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('formola', '0008_auto_20201229_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='User',
        ),
        migrations.RemoveField(
            model_name='formola',
            name='_Vahed',
        ),
        migrations.RemoveField(
            model_name='formola',
            name='_water',
        ),
        migrations.RemoveField(
            model_name='formola',
            name='meghdar',
        ),
        migrations.AddField(
            model_name='formola',
            name='ahan',
            field=models.CharField(blank=True, help_text='آهن', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='asidborik',
            field=models.CharField(blank=True, help_text='اسید بوریک', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='bor',
            field=models.CharField(blank=True, help_text='بور', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='calsiom',
            field=models.CharField(blank=True, help_text='کلسیم', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='content',
            field=djrichtextfield.models.RichTextField(default='null', help_text='توضیحات اضافه'),
        ),
        migrations.AddField(
            model_name='formola',
            name='diamoniomfosfat',
            field=models.CharField(blank=True, help_text='دی آمونیوم فسفات', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='fosfat',
            field=models.CharField(blank=True, help_text='فسفات', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='fosfor',
            field=models.CharField(blank=True, help_text='فسفر', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='gogerd',
            field=models.CharField(blank=True, help_text='گوگرد', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='kalat_ahan',
            field=models.CharField(blank=True, help_text='کلات آهن', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='manganez',
            field=models.CharField(blank=True, help_text='منگنز', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='maniaziom',
            field=models.CharField(blank=True, help_text='منیزیم', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='mes',
            field=models.CharField(blank=True, help_text='مس', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='molibden',
            field=models.CharField(blank=True, help_text='مولیبدن', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='nitrat_calsiom',
            field=models.CharField(blank=True, help_text='نیترات کلسیم', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='nitrat_potasiom',
            field=models.CharField(blank=True, help_text='نیترات پتاسیم', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='nitratamoniom',
            field=models.CharField(blank=True, help_text='نیترات آمونیم', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='nitrozhen',
            field=models.CharField(blank=True, help_text='نیتروژن', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='nitrozhenamoniomi',
            field=models.CharField(blank=True, help_text='نیتروژن آمونیومی', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='nitrozhennitarti',
            field=models.CharField(blank=True, help_text='نیتروژن نیتراتی', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='ore',
            field=models.CharField(blank=True, help_text='اوره', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='potasiom',
            field=models.CharField(blank=True, help_text='پتاسیم', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='potasiomfosfat',
            field=models.CharField(blank=True, help_text='پتاسیم فسفات', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='potasiomoksid',
            field=models.CharField(blank=True, help_text='پتاسیم اکسید', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='roshd_time',
            field=models.CharField(choices=[('KB', 'کشت بهاره'), ('KP', 'کشت پاییزه'), ('GK', 'قبل کشت'), ('RR', 'رشد رویشی'), ('GD', 'گلدهی و تشکیل میوه'), ('AM', 'مرحله رشدي گیاهچه تا تشکیل اولین میوه'), ('EB', 'مرحله رشدي تشکیل میوه تا اتمام برداشت '), ('DH', 'دو هفته اول'), ('RY', 'رشد رویشی'), ('GM', 'گلدهی تا تشکیل اولین میوه'), ('TB', 'تشکیل میوه تا اولین برداشت'), ('NT', 'نشا تا ظهور اولین گل'), ('BG', 'بعد از گلدهی'), ('PA', 'پس از کاشت'), ('RM', 'رشد میوه'), ('CA', 'چین اول'), ('CD', 'چین دوم'), ('CS', 'چین سوم'), ('AB', 'آخرین برداشت')], default='GK', max_length=2),
        ),
        migrations.AddField(
            model_name='formola',
            name='roy',
            field=models.CharField(blank=True, help_text='روی', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='sokesterinahan',
            field=models.CharField(blank=True, help_text='سوکسترین آهن', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='solfat_manianziom',
            field=models.CharField(blank=True, help_text='سولفات منیزیم', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='solfatmanganez',
            field=models.CharField(blank=True, help_text='سولفات منگنز', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='solfatmaniaziom',
            field=models.CharField(blank=True, help_text='سولفات منیزیم', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='solfatmes',
            field=models.CharField(blank=True, help_text='سولفات مس', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='solfatroy',
            field=models.CharField(blank=True, help_text='سولفات روی', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='formola',
            name='soperfosfattripl',
            field=models.CharField(blank=True, help_text='سوپر فسفات پربپل', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formola',
            name='name',
            field=models.CharField(help_text='نام گیاه', max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='farmer',
        ),
    ]
