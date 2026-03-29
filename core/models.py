from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(verbose_name="Дата и время")
    image = models.ImageField(upload_to='events/', verbose_name="Фото")
    registration_url = models.URLField(blank=True, verbose_name="Ссылка на регистрацию")

    def __str__(self):
        return self.title

class PartnerPhoto(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name="Заголовок/Описание")
    image = models.ImageField(upload_to='partners/vinogradova/', verbose_name="Файл изображения")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    class Meta:
        verbose_name = "Фото Ирины Виноградовой"
        verbose_name_plural = "Галерея Ирины Виноградовой"

    def __str__(self):
        return self.title or f"Фото №{self.id}"