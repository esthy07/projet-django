from django.contrib import admin
from myapp.models import user
from myapp.models import Internaute
from myapp.models import choix
from myapp.models import Pari

# Register your models here.
admin.site.register(user)
admin.site.register(Internaute)
admin.site.register(choix)
admin.site.register(Pari)
