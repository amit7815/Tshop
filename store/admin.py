from django.contrib import admin
from store.models import Tshirt, Color, Sleeve, Brand, NeckType, IdealFor, Occasion 

admin.site.register([Tshirt, Color, Sleeve, Brand, NeckType, IdealFor, Occasion 
])

# Register your models here.
