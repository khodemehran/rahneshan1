from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.
class formola(models.Model):
    GERAM = 'GER'
    MILIGRAM = 'MIL'
    KILOGRAM = 'KIL'
    PEYMANE = 'PEY'


    MEGHDAR_CHOICES = [

            (GERAM,'گرم'),
            (MILIGRAM,'میلی گرم'),
            (KILOGRAM,'کیلو گرم'),
            (PEYMANE,'پیمانه'),

                      ]
    FOSFOR = 'FOS'
    NITRO = 'NIT'
    SODIOM = 'NAC'
    AHAN = 'FEA'


    KOD_CHO = [

            (FOSFOR,'فسفر'),
            (NITRO, 'نیتروژن'),
            (AHAN,'آهن'),
            (SODIOM,'سدیم'),

            ]
    name = models.CharField(max_length=3, choices=KOD_CHO ,help_text='نام کود')
    _water = models.IntegerField(max_length=25,help_text='مقدار در آب')
    _Vahed = models.CharField(max_length=3,choices=MEGHDAR_CHOICES)
    meghdar = models.IntegerField(max_length=25, help_text='مقدار کود')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'نام کود ->' + self.name
    
    class Meta:
        db_table = 'فرمولاسیون'
        ordering = ['-created_at']


class farmer(models.Model):

