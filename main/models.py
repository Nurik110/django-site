from django.db import models
from PIL import Image

# Create your models here.

# боец
# маг
# танк
# ассасин
# поддержка
class Heroes(models.Model):
    Fighter = 'fighter' 
    Magician = 'magician'
    Assassin = 'assassin'
    Tank = 'tank'
    Support = 'support'
    Shooter = 'shooter'
    CHOICE_GROUP = {
        (Fighter, 'fighter'), 
        (Magician, 'magician'),
        (Assassin, 'assassin'),
        (Tank, 'tank'),
        (Support, 'support'),
        (Shooter, 'shooter'),
    }
    id = models.IntegerField(verbose_name='Айди', primary_key = True)
    name = models.CharField(max_length=255, verbose_name='Имя')
    price = models.IntegerField(verbose_name='Цена')
    classs = models.CharField(max_length=255, verbose_name='Класс', default = "Класс")
    description = models.TextField(verbose_name='Описания')
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default = Fighter, verbose_name='Группа')
    img = models.ImageField(default = 'noimage.jpg', upload_to='heroes_image', verbose_name='Фото')

    def __str__(self):
        return f'{self.name}'

class Images(models.Model):
    id = models.IntegerField(verbose_name='ID', primary_key = True)
    post = models.ForeignKey(Heroes, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='heroes_image')

    def __str__(self):
        return f'{self.image}'
    
class Equipment(models.Model):
    magatt = 'magatt' 
    physatt = 'physatt'
    deff = 'deff'
    CHOICE_GROUP = {
        (magatt, 'magatt'), 
        (physatt, 'physatt'),
        (deff, 'deff'),
    }
    id = models.IntegerField(verbose_name='ID', primary_key = True)
    image = models.ImageField(upload_to='heroes_image')
    name = models.CharField(max_length=255, verbose_name='Имя')
    price = models.IntegerField(verbose_name='Цена')
    classs = models.CharField(max_length=25, choices=CHOICE_GROUP, verbose_name='Класс', default = "magatt")
    description = models.TextField(verbose_name='Описания')

    def __str__(self):
        return f'{self.name}'

class Feature(models.Model):
    id = models.IntegerField(verbose_name='ID', primary_key = True)
    name = models.ForeignKey(Heroes, default=None, on_delete=models.CASCADE,verbose_name='Имя')
    hp = models.IntegerField(verbose_name='ХП')
    hp_regen = models.IntegerField(verbose_name='ХП реген')
    mp = models.IntegerField(verbose_name='МП')
    mana_regen = models.IntegerField(verbose_name='Мага реген')
    phyatt = models.IntegerField(verbose_name='Физическая атака')
    phydef = models.IntegerField(verbose_name='Физическая защита')
    magatt = models.IntegerField(verbose_name='Магическая атака')
    magdef = models.IntegerField(verbose_name='Магическая защита')
    mov_speed = models.IntegerField(verbose_name='Скорость передвижение')
    att_speed = models.IntegerField(verbose_name='Скорость атаки')
    phy_vam = models.IntegerField(verbose_name='Физический вампиризм')
    mag_vam = models.IntegerField(verbose_name='Магический вампиризм')
    bas_atk_crit = models.IntegerField(verbose_name='Базовая вероятность критического удара')
    ability_crit = models.IntegerField(verbose_name='Вероятность критического удара способностей')

    def __str__(self):
        return f'{self.name}'

class Ability(models.Model):
    id = models.IntegerField(verbose_name='Айди', primary_key = True)
    name = models.ForeignKey(Heroes, default=None, on_delete=models.CASCADE,verbose_name='Имя')
    description = models.TextField(verbose_name='Описания')
    img = models.ImageField(default = 'noimage.jpg', upload_to='heroes_image', verbose_name='Фото')

    def __str__(self):
        return f'{self.name}'