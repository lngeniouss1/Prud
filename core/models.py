from django.db import models
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    image_url = models.URLField()  # Ссылка на картинку
    registration_url = models.URLField() # Ссылка для кнопки "Записаться"

    def __str__(self):
        return self.title
