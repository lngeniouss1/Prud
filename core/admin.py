from django.contrib import admin
from .models import Event, PartnerPhoto
from django.utils.safestring import mark_safe

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'registration_url')
    search_fields = ('title',)
@admin.register(PartnerPhoto)
class PartnerPhotoAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'uploaded_at')
    list_display_links = ('get_image', 'title')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-cover: cover; border-radius: 4px;" />')
        return "Нет фото"
    
    get_image.short_description = "Превью"