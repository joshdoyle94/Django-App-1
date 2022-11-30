from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} {self.name}"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'sport': self.sport,
        }