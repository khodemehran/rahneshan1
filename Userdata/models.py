from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PlanetData(models.Model):

    # choices for four weather climate of IRAN
    SARD_KOHESTANI = 'KOH'
    MOTADEL = 'MOT'
    GARM_KHOSHK = 'GKH'
    GARM_MARTOB = 'GMA'


    WEATHER_CHOICES = [

            (SARD_KOHESTANI, 'کوهستانی'),
            (MOTADEL,'معتدل'),
            (GARM_KHOSHK,'گرم و خشک'),
            (GARM_MARTOB,'گرم و مرطوب'),

                      ]
    DEYM = 'DEM'
    ABI = 'ABI'

    WATER_CHOICES = [
            (DEYM, 'دیم'),
            (ABI, 'آبی'),
                    ]

    BAGHI = 'BAQ'
    GOLKHANE = 'GOL'
    ZERAEI = 'ZER'


    PLANET_CHOICES = [
        
    (BAGHI, "باغی"),
    (ZERAEI, "زراعی"),
    (GOLKHANE,"گلخانه ای"),

                     ]
    
    #define models here 
    Category = models.CharField(max_length=3,choices=PLANET_CHOICES, default="GOLKHANE")
    User = models.ForeignKey(User, on_delete = models.CASCADE)
    Name = models.CharField(max_length=150,help_text='نام گیاه')
#   Categories = models.ManyToManyField(Category)
    Age_Stirng = models.CharField(max_length=4,
                                 help_text='اگر سن گیاه به صورت بخش بندی باشد', 
                                blank = True,
                                    )
    Age_Numberic = models.IntegerField(help_text='اگر سن گیاه به صورت عددی باشد.')
    Weather = models.CharField(max_length=3,
                                help_text='شرایط آب و هوایی منطقه کاربر.',
                                choices=WEATHER_CHOICES,
                                default=MOTADEL,
                                    )
    Water = models.CharField(max_length=3,
                            help_text="شرایط آبیاری گیاه",
                            choices=WATER_CHOICES,
                            default=DEYM,
                                )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Area = models.FloatField()

    #return name of instance
    
    def __str__(self):
        return self.Name

    #order by last instance

    class Meta:
        db_table = 'اطلاعات گیاه'
        ordering = ['-created_at']
        
    

class Contact(models.Model):

    name = models.CharField(max_length=254)
    Email_field = models.EmailField(max_length=254)
    content = models.CharField(max_length=254)


    def str(self):
        return self.name
    

    