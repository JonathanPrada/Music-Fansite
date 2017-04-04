from __future__ import unicode_literals
# Access the database
from django.db import models
# Gets URL
from django.core.urlresolvers import reverse


# Our music table blueprints here
class Album(models.Model):
    artist = models.CharField(max_length=255)
    album_title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    # Allows uploading of images
    album_logo = models.FileField()

    # When a new album submitted, a new url with the pk gets returned
    def get_absolute_url(self):
        # Pass in pk to DetailView in views.py through url.py
        return reverse('music:detail', kwargs={'pk': self.pk})

    # When requested through shell, do a string representation
    # of the columns included in the definition
    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    # this links the song to the album it belongs by storing an album key here
    # if you delete the album it belongs to, the songs also disappear
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    # When requested through shell, do a string representation
    # of the columns included in the definition
    def __str__(self):
        return self.song_title
