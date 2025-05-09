from django.db import models

class SongInformation(models.Model):
    Title = models.CharField(max_length=255, null=True, blank=True)
    Id_number = models.IntegerField(null=True, blank=True)
    Artists = models.CharField(max_length=255, null=True, blank=True)
    Movie = models.CharField(max_length=255, null=True, blank=True)
    Track = models.FileField(null=True, blank=True)
    # Picture = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title



class ArtistInformation(models.Model):
    Name = models.CharField(max_length=255, null=True, blank=True)
    Id_number = models.IntegerField(null=True, blank=True)
    Genres = models.CharField(max_length=255, null=True, blank=True)
    Image = models.FileField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.Title

class MovieInformation(models.Model):
    Name = models.CharField(max_length=255, null=True, blank=True)
    Image = models.FileField(max_length=255, null=True, blank=True)
    Id_number = models.IntegerField(null=True, blank=True)



