from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Testtaker)
admin.site.register(models.Testsetter)
admin.site.register(models.Testadmin)