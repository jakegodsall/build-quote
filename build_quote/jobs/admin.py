from django.contrib import admin
from . import models

admin.site.register(models.Address)
admin.site.register(models.Customer)
admin.site.register(models.Spec)
admin.site.register(models.Job)
admin.site.register(models.Quotation)
admin.site.register(models.Invoice)