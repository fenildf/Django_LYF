from django.contrib import admin
from .models import Moment

class MomentAdmin(admin.ModelAdmin):
    empty_value_display = "空值"

admin.site.register(Moment)

# Register your models here.
