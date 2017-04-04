from django.shortcuts import render, get_object_or_404
from .models import Album, Song


# Homepage
def index(request):
    # Connect to the database and get albums
    all_albums = Album.objects.all()
    # Use all_albums to pass in a dictionary of information to template
    # Render the template and pass in a dictionary
    return render(request, 'music/index.html', {'all_albums': all_albums})


# Show album details, pass in album id from url
def detail(request, album_id):
    # Try to query the database, use the album id passed in
    # If album does not exist raise a 404
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


# Receives the favorite song from the form
def favorite(request, album_id):
    # Try to query the database, use the album id passed in
    # If album does not exist raise a 404
    album = get_object_or_404(Album, pk=album_id)
    try:
        # From the form's name="song" submitted, get the value={{ song.id }}
        selected_song = album.song_set.get(pk=request.POST['song'])
    # If an invalid selection or no song selected is made
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album,
                                                     'error_message': "You did not select a valid song"
                                                     })
    # If everything goes smoothly
    else:
        # Change the selected song's favorite attribute to true
        selected_song.is_favorite = True
        # Save to the database
        selected_song.save()
        # Render the page again with the new content
        return render(request, 'music/detail.html', {'album': album})


