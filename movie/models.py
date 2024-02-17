from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.genre

class Director(models.Model):
    director = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.director


class Title(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField()
    poster = models.ImageField(upload_to='', null=True)

    def __str__(self) -> str:
        return self.name
    
    def genre_list(self):
        return list(self.genre.values_list('genre', flat=True))
