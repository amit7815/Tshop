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



