from django.contrib import admin

from . import models

admin.site.register(models.Incoming)
admin.site.register(models.ChangeStatus)