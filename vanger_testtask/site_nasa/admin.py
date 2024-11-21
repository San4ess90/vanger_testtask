from django.contrib import admin
from .models import Slider
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html

@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_display', 'thumbnail_display', 'order')
    search_fields = ['title']

    def image_display(self, obj):
        return format_html('<img src="{}" width="100" />', obj.image.url if obj.image else '')

    def thumbnail_display(self, obj):
        return format_html('<img src="{}" width="50" />', obj.thumbnail.url if obj.thumbnail else '')

    image_display.short_description = 'Изображение'
    thumbnail_display.short_description = 'Миниатюра'


