from django.contrib import admin

from .models import Census


class CensusAdmin(admin.ModelAdmin):
    filter_horizontal = ('voters', )


admin.site.register(Census, CensusAdmin)
