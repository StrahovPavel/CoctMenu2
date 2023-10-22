from django.db import models

class Coct(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField()
    price = models.IntegerField()
    time_create=models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title



    class Meta:
        verbose_name="Коктейли"
        verbose_name_plural="Коктейли"
        ordering = ["time_create", "title"]