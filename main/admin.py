from django.contrib import admin
from .models import Heroes
from .models import Images
from .models import Equipment
from .models import Feature
from .models import Ability

# Register your models here.

admin.site.register(Heroes)
admin.site.register(Images)
admin.site.register(Equipment)
admin.site.register(Feature)
admin.site.register(Ability)



