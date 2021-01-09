# Generated by Django 3.1.2 on 2021-01-09 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formola', '0011_auto_20210110_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinput',
            name='Roshd_date',
            field=models.CharField(choices=[('KB', 'کشت بهاره'), ('KP', 'کشت پاییزه'), ('GK', 'قبل کشت'), ('RR', 'رشد رویشی'), ('GD', 'گلدهی و تشکیل میوه'), ('AM', 'مرحله رشدي گیاهچه تا تشکیل اولین میوه'), ('EB', 'مرحله رشدي تشکیل میوه تا اتمام برداشت '), ('DH', 'دو هفته اول'), ('RY', 'رشد رویشی'), ('PS', 'مرحله تشکیل و پر شدن غده'), ('BG', 'بلوغ غده'), ('GM', 'گلدهی تا تشکیل اولین میوه'), ('TB', 'تشکیل میوه تا اولین برداشت'), ('NT', 'نشا تا ظهور اولین گل'), ('BA', 'بعد از گلدهی'), ('PA', 'پس از کاشت'), ('RM', 'رشد میوه'), ('CA', 'چین اول'), ('CD', 'چین دوم'), ('CS', 'چین سوم'), ('AB', 'آخرین برداشت')], default='KB', max_length=2),
        ),
        migrations.AlterField(
            model_name='userinput',
            name='name',
            field=models.CharField(choices=[('KG', 'خیار گلخانه'), ('KM', 'خیار مذرعه'), ('KH', 'خیار هیدروپونیک'), ('FM', 'فلفل دلمه مزرعه'), ('FH', 'فلفل دلمه هیدرو پونیک'), ('GM', 'گوجه فرنگی مذرعه'), ('GH', 'گوجه فرنگی هیدروپونیک '), ('GG', 'گوجه گلخانه ای'), ('SZ', 'سیب زمینی')], default='KG', max_length=2),
        ),
    ]