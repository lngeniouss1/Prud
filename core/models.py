from django.db import models
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
    # Список партнеров для выбора в админке
    PARTNER_CHOICES = [
        ('vinogradova', 'Ирина Виноградова'),
        ('IET', 'Институт экономики и туризма'),
        ('BPS', 'Отряд имени Андрея Дубенского'),
    ]

    partner_slug = models.CharField(
        max_length=50, 
        choices=PARTNER_CHOICES, 
        default='vinogradova',
        verbose_name="К какому партнеру относится?"
    )
    title = models.CharField(max_length=200, blank=True, verbose_name="Подпись (необязательно)")
    image = models.ImageField(upload_to='partners/', verbose_name="Фотография")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Фото партнера"
        verbose_name_plural = "Галерея партнеров"

    def __str__(self):
        return f"{self.get_partner_slug_display()} - {self.title or self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

            max_size = (1600, 1600)
            if img.width > 1600 or img.height > 1600:
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            img.save(img_path, "JPEG", quality=75, optimize=True)