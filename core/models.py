from django.db import migrations, models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='events/') 
    registration_url = models.URLField(blank=True)

    def __clstr__(self):
        return self.title
