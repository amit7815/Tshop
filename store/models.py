from django.db import models

# Create your models here.
class TshirProperty(models.Model):
    ''' parent for tshirt properties '''
    title = models.CharField(max_length = 30, null = False)
    slug = models.CharField(max_length = 30, null = False, unique = True)

    def __str__(self):
        return self.title

    class Meta:   # due to we don't want to add this as database table(abstract base class)
        abstract = True

class Occasion(TshirProperty):
    ''' Store ocassion like Sports , Party wear and so on '''
    pass


class IdealFor(TshirProperty):
    '''Stores who is best suited like Men , Women, Kids '''
    pass

class NeckType(TshirProperty):
    ''' Stores what is the necktype of tshirt like round or V'''
    pass


class Brand(TshirProperty):
    '''Stores brand of Tshirt'''
    pass

class Sleeve(TshirProperty):
    ''' Stores sleeve like half, full'''
    pass

class Color(TshirProperty):
    '''Stores color of Tshirt'''
    pass


class Tshirt(models.Model):
    ''' Model for Tshirt '''
    name = models.TextField(max_length = 50, null = False)
    description = models.CharField(max_length = 500, null = False)
    discount = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = 'upload/images', null = False)
    occassion = models.ForeignKey(Occasion, on_delete =  models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete =  models.CASCADE)
    color = models.ForeignKey(Color, on_delete =  models.CASCADE)
    neck_type = models.ForeignKey(NeckType,on_delete =  models.CASCADE)
    idealFor = models.ForeignKey(IdealFor, on_delete =  models.CASCADE)
    



