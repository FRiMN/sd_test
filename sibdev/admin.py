from django.contrib import admin

from sibdev.models import UrlQueue


@admin.register(UrlQueue)
class UrlQueueAdmin(admin.ModelAdmin):
    list_display = ('url', 'timeshift', 'done')