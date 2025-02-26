from django.urls import path
from .views import home, FileUploadView, getSongInfos, getArtists, getArtistInfos, getmovie, getMovieInfo, update_artists, delete_artist, delete_movie, delete_song
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('submit/', FileUploadView, name='upload-data'),
    path('songinfos/', getSongInfos),
    path('a-submit/', getArtists),
    path('artistsinfos/', getArtistInfos),
    # path('alb-submit/', getAlbum),
    # path('albuminfo/', getAlbumInfo),
    path('m-submit/', getmovie),
    path('movieinfo/', getMovieInfo),
    path("update-artists/<int:artist_id>/", update_artists, name="update_artists"),
    path("delete-artist/<int:artist_id>/", delete_artist, name="delete_artist"),
    path("delete-movie/<int:movie_id>/", delete_movie, name="delete_movie"),
    path("delete-song/<int:song_id>/", delete_song, name="delete_movie"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
