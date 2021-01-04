from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from djrichtextfield.models import RichTextField

# Create your models here.
    #def __str__(self):
        #return self.Name
    #def get_absulote_url(self):
     #   return reverse('category',args=[self.slug])
   # class Meta:
    #    verbose_name_plural = 'Categories'

class formola(models.Model):

    class roshd(models.TextChoices):
        KESHT_BAHARE = 'KB', _('کشت بهاره')
        KESHT_PAYIZE = 'KP', _('کشت پاییزه')
        GHABL_KESHT = 'GK', _('قبل کشت')
        ROSHD_ROYESHI = 'RR', _('رشد رویشی')
        GOL_DEHI = 'GD', _('گلدهی و تشکیل میوه')
        AVALIN_MIVE = 'AM',_('مرحله رشدي گیاهچه تا تشکیل اولین میوه')
        ETMAM_BARDASHT = 'EB',_('مرحله رشدي تشکیل میوه تا اتمام برداشت ')
        DO_HAFTE_AVAL = 'DH',_('دو هفته اول')
        ROSH_ROYESHI = 'RY',_('رشد رویشی')
        GOL_DEHI_TA_AVALIN_MIVE = 'GM',_('گلدهی تا تشکیل اولین میوه')
        TASHKIL_MIVE_TA_BARDASHT = 'TB',_('تشکیل میوه تا اولین برداشت')
        NESHA_TA_AVALIN_GOL = 'NT',_('نشا تا ظهور اولین گل')
        BAD_AZ_GOLDEHI = 'BG',_('بعد از گلدهی')
        PAS_AZ_KASHT = 'PA',_('پس از کاشت')
        ROSHD_MIVE = 'RM',_('رشد میوه')
        CHIN_AVAL = 'CA',_('چین اول')
        CHIN_DOVOM = 'CD',_('چین دوم')
        CHIN_SEVOM = 'CS',_('چین سوم')
        AKHARIN_BARDASHT = 'AB',_('آخرین برداشت')
    class Name(models.TextChoices):
        KHIAR_GOL = 'KG', _('خیار گلخانه')
        KHIAR_MAZRAE = 'KM', _('خیار مذرعه')
        KHIAR_HIDRO = 'KH', _('خیار هیدروپونیک')
        FELFEL_MAZRAE = 'FM', _('فلفل دلمه مزرعه')
        FELFEL_HIDRO = 'FH', _('فلفل دلمه هیدرو پونیک')
        GOJE_MAZRAE = 'GM',_('گوجه فرنگی مذرعه')
        GOJE_HIDRO = 'GH',_('گوجه فرنگی هیدروپونیک ')
    roshd_time = models.CharField(max_length=2, choices
    =roshd.choices,default=roshd.GHABL_KESHT)
    name = models.CharField(max_length=2, choices=Name.choices,default=Name.KHIAR_GOL)
    solfat_manianziom = models.CharField(max_length=100,help_text='سولفات منیزیم' ,null=True, blank=True)
    nitrat_potasiom = models.CharField(max_length=100,help_text='نیترات پتاسیم' ,null=True, blank=True)
    nitrat_calsiom = models.CharField(max_length=100,help_text='نیترات کلسیم' ,null=True, blank=True)
    kalat_ahan = models.CharField(max_length=100,help_text='کلات آهن', null=True, blank=True)
    nitrozhen = models.CharField(max_length=100,help_text='نیتروژن', null=True, blank=True)
    fosfor = models.CharField(max_length=100,help_text='فسفر', null=True, blank=True)
    potasiom = models.CharField(max_length=100,help_text='پتاسیم', null=True, blank=True) 
    calsiom = models.CharField(max_length=100,help_text='کلسیم', null=True, blank=True)   
    maniaziom = models.CharField(max_length=100,help_text='منیزیم', null=True, blank=True)
    ore = models.CharField(max_length=100,help_text='اوره', null=True, blank=True)
    diamoniomfosfat = models.CharField(max_length=100,help_text='دی آمونیوم فسفات', null=True, blank=True)
    soperfosfattripl = models.CharField(max_length=100,help_text='سوپر فسفات پربپل', null=True, blank=True)
    sokesterinahan = models.CharField(max_length=100,help_text='سوکسترین آهن', null=True, blank=True)
    solfatmanganez = models.CharField(max_length=100,help_text='سولفات منگنز', null=True, blank=True)
    solfatroy = models.CharField(max_length=100,help_text='سولفات روی', null=True, blank=True)
    solfatmes = models.CharField(max_length=100,help_text='سولفات مس', null=True, blank=True)
    asidborik = models.CharField(max_length=100,help_text='اسید بوریک', null=True, blank=True)
    solfatmaniaziom = models.CharField(max_length=100,help_text='سولفات منیزیم', null=True, blank=True)
    potasiomfosfat = models.CharField(max_length=100,help_text='پتاسیم فسفات', null=True, blank=True)
    nitratamoniom = models.CharField(max_length=100,help_text='نیترات آمونیم', null=True, blank=True)
    potasiomoksid = models.CharField(max_length=100,help_text='پتاسیم اکسید', null=True, blank=True)
    fosfat = models.CharField(max_length=100,help_text='فسفات', null=True, blank=True)
    nitrozhennitarti = models.CharField(max_length=100,help_text='نیتروژن نیتراتی', null=True, blank=True)
    nitrozhenamoniomi = models.CharField(max_length=100,help_text='نیتروژن آمونیومی', null=True, blank=True)
    gogerd = models.CharField(max_length=100,help_text='گوگرد', null=True, blank=True)
    bor = models.CharField(max_length=100,help_text='بور', null=True, blank=True)
    mes = models.CharField(max_length=100,help_text='مس', null=True, blank=True)
    manganez = models.CharField(max_length=100,help_text='منگنز', null=True, blank=True)
    molibden = models.CharField(max_length=100,help_text='مولیبدن', null=True, blank=True)   
    roy = models.CharField(max_length=100,help_text='روی', null=True, blank=True)
    ahan = models.CharField(max_length=100, help_text='آهن', null=True, blank=True)
    content = RichTextField(help_text='توضیحات اضافه', default= 'null')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.get_name_display() +'|'+ self.get_roshd_time_display()

    



class userinput(models.Model):

    class Roshd(models.TextChoices):
        KESHT_BAHARE = 'KB', _('کشت بهاره')
        KESHT_PAYIZE = 'KP', _('کشت پاییزه')
        GHABL_KESHT = 'GK', _('قبل کشت')
        ROSHD_ROYESHI = 'RR', _('رشد رویشی')
        GOL_DEHI = 'GD', _('گلدهی و تشکیل میوه')
        AVALIN_MIVE = 'AM',_('مرحله رشدي گیاهچه تا تشکیل اولین میوه')
        ETMAM_BARDASHT = 'EB',_('مرحله رشدي تشکیل میوه تا اتمام برداشت ')
        DO_HAFTE_AVAL = 'DH',_('دو هفته اول')
        ROSH_ROYESHI = 'RY',_('رشد رویشی')
        GOL_DEHI_TA_AVALIN_MIVE = 'GM',_('گلدهی تا تشکیل اولین میوه')
        TASHKIL_MIVE_TA_BARDASHT = 'TB',_('تشکیل میوه تا اولین برداشت')
        NESHA_TA_AVALIN_GOL = 'NT',_('نشا تا ظهور اولین گل')
        BAD_AZ_GOLDEHI = 'BG',_('بعد از گلدهی')
        PAS_AZ_KASHT = 'PA',_('پس از کاشت')
        ROSHD_MIVE = 'RM',_('رشد میوه')
        CHIN_AVAL = 'CA',_('چین اول')
        CHIN_DOVOM = 'CD',_('چین دوم')
        CHIN_SEVOM = 'CS',_('چین سوم')
        AKHARIN_BARDASHT = 'AB',_('آخرین برداشت')
    class Name(models.TextChoices):
        KHIAR_GOL = 'KG', _('خیار گلخانه')
        KHIAR_MAZRAE = 'KM', _('خیار مذرعه')
        KHIAR_HIDRO = 'KH', _('خیار هیدروپونیک')
        FELFEL_MAZRAE = 'FM', _('فلفل دلمه مزرعه')
        FELFEL_HIDRO = 'FH', _('فلفل دلمه هیدرو پونیک')
        GOJE_MAZRAE = 'GM',_('گوجه فرنگی مذرعه')
        GOJE_HIDRO = 'GH',_('گوجه فرنگی هیدروپونیک ')

    Roshd_date = models.CharField(max_length=2,choices=Roshd.choices,default=Roshd.KESHT_BAHARE)
    name = models.CharField(max_length=2, choices=Name.choices,default=Name.KHIAR_GOL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name