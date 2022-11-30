from django.db import models

# Create your models here.
class VideoGame(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} is a {self.genre} and has a rating of {self.rating}"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre,
            'rating': self.rating,
        }