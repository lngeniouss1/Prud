from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import PartnerPhoto, Event

@admin.register(PartnerPhoto)
class PartnerPhotoAdmin(admin.ModelAdmin):
    list_display = ('get_preview', 'partner_slug', 'title', 'has_video', 'uploaded_at')
    
    list_filter = ('partner_slug', 'uploaded_at')
    
    search_fields = ('title', 'partner_description')
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('partner_slug', 'partner_description')
        }),
        ('Контент', {
            'fields': ('title', 'image', 'video_file'),
            'description': 'Загрузите фото. Если загрузите видео, фото станет его обложкой.'
        }),
    )

    def get_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit:cover; border-radius:4px;">')
        return "Нет фото"
    get_preview.short_description = "Превью"

    def has_video(self, obj):
        return bool(obj.video_file)
    has_video.boolean = True
    has_video.short_description = "Видео"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'registration_url')
    list_filter = ('date',)
    search_fields = ('title', 'description')