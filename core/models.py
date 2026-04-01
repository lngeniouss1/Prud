from django.db import models
from django.core.validators import FileExtensionValidator
from PIL import Image
import os

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(verbose_name="Дата и время")
    image = models.ImageField(upload_to='events/', verbose_name="Фото")
    registration_url = models.URLField(blank=True, verbose_name="Ссылка на регистрацию")

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.title

class PartnerPhoto(models.Model):
    PARTNER_CHOICES = [
        ('NarodnFront', 'Алексей Мокеев'),
        ('RGO', 'Молодёжный клуб РГО «Владимир»'),
        ('BPS', 'БПС г.Владимир. Отряд имени Андрея Дубенского'),
        ('Veles', 'Велотур клуб "ВЕЛЕС"'),
        ('IET', 'Институт экономики и туризма'),
        ('ARH', 'Институт архитектуры, строительства и энергетики'),
        ('School', 'МБОУ СОШ №19'),
        ('vinogradova', 'Ирина Виноградова'),
    ]

    partner_slug = models.CharField(
        max_length=50, 
        choices=PARTNER_CHOICES, 
        default='vinogradova',
        verbose_name="Партнер"
    )
    title = models.CharField(max_length=200, blank=True, verbose_name="Подпись")

    partner_description = models.TextField(
        blank=True, 
        verbose_name="Описание партнера", 
        help_text="Достаточно заполнить только у ОДНОЙ фотографии партнера, чтобы текст появился в заголовке раздела."
    )
    
    image = models.ImageField(upload_to='partners/photos/', verbose_name="Фото")
    video_file = models.FileField(upload_to='partners/videos/', null=True, blank=True, verbose_name="Видео")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    image = models.ImageField(
        upload_to='partners/photos/', 
        verbose_name="Фото (или превью для видео)"
    )
    
    video_file = models.FileField(
        upload_to='partners/videos/',
        null=True,
        blank=True,
        verbose_name="Видео файл (MP4/MOV)",
        help_text="Оставьте пустым, если хотите добавить только фото",
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'webm'])]
    )
    
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Медиа партнера"
        verbose_name_plural = "Медиа партнеров"
        ordering = ['uploaded_at']

    def __str__(self):
        return f"{self.get_partner_slug_display()} - {self.title or self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            try:
                img = Image.open(img_path)
                
                max_size = (1600, 1600)
                if img.width > 1600 or img.height > 1600:
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                img.save(img_path, "JPEG", quality=75, optimize=True)
            except Exception as e:
                print(f"Ошибка сжатия изображения: {e}")