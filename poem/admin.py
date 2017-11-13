from django.contrib import admin
from . import models
# Register your models here.



admin.site.register(models.Poem)
admin.site.register(models.Author)
admin.site.register(models.Tags)
admin.site.register(models.Category)

