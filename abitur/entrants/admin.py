from django.contrib import admin

from .models import *


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


admin.site.register(Services, ServicesAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization_key', 'specialization', 'overall_rating')
    list_display_links = ('id', 'name')
    search_fields = ('specialization',)
    list_filter = ('overall_rating', 'specialization',)

    def specialization_key(self, obj):
        return obj.specialization[0:4]

    specialization_key.short_description = 'Факультет'


admin.site.register(Application, ApplicationAdmin)
