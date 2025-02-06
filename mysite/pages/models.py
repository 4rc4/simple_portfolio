from django.db import models

class PorscheModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='models/')  # Görseller için
    description = models.TextField()  # Uzun açıklamalar için

    def __str__(self):
        return self.name
