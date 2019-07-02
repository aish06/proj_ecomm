from django.contrib import admin

from .models import Cake


class cakeadmin(admin.ModelAdmin):
    list_display = ['__str__','cake_id']
    class Meta:
        model=Cake


admin.site.register(Cake,cakeadmin)





