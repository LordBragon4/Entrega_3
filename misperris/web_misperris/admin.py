from django.contrib import admin

# Register your models here.

from .models import Rescatado
from .models import Usuario

admin.site.register(Rescatado)
admin.site.register(Usuario)