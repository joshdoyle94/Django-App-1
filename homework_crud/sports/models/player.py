from django.db import models
from .team import Team

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number = models.IntegerField(max_length=100)
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        related_name='teams_played_for'
    )
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} is number {self.number}"

    def as_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'number': self.number,
        }