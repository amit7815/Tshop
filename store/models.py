from django.db import models

# Create your models here.
class Occasion(models.Model):
    ''' Store ocassion like Sports , Party wear and so on '''
    title = models.CharField(max_length = 20, null = False)
    slug = models.CharField(max_length = 30, null= False)


class IdealFor(models.Model):
    '''Stores who is best suited like Men , Women, Kids '''
    title = models.CharField(max_length = 30, null = False)
    slug = models.CharField(max_length = 30, null = False)

class NeckType(models.Model):
    ''' Stores what is the necktype of tshirt like round or V'''
    title = models.CharField(max_length = 30, null = False)
    slug = models.CharField(max_length = 30, null = False)


class Brand(models.Model):
    '''Stores brand of Tshirt'''
    title = models.CharField(max_length = 30, null = False)
    slug = models.CharField(max_length = 30, null = False)

class Sleeve(models.Model):
    ''' Stores sleeve like half, full'''
    title = models.CharField(max_length = 30, null = False)
    slug = models.CharField(max_length = 30, null = False)

class Color(models.Model):
    '''Stores color of Tshirt'''
    title = models.CharField(max_length = 30, null = False)
    slug = models.CharField(max_length = 30, null = False)


class Tshirt(models.Model):
    name = models.TextField(max_length = 50, null = False)
    description = models.CharField(max_length = 500, null = False)
    discount = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = '/upload/images', null = False)
    occassion = models.ForeignKey(Occasion, on_delete =  models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete =  models.CASCADE)
    color = models.ForeignKey(Color, on_delete =  models.CASCADE)
    neck_type = models.ForeignKey(NeckType,on_delete =  models.CASCADE)
    idealFor = models.ForeignKey(IdealFor, on_delete =  models.CASCADE)
    



