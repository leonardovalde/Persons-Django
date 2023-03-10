from django.contrib import admin

from personas.models import Domicilio, Personas

admin.site.register([Personas, Domicilio])
