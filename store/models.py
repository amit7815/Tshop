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





