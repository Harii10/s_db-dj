from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SongInformation, ArtistInformation, AlbumInformation, MovieInformation, TrackModel  
from .serializers import SongDataSerializer
from django.shortcuts import render



def home(request):
    return render(request, 'index.html')

# Songs
@api_view(["GET", "POST"])
# @csrf_exempt
def FileUploadView(request):
    if request.method == "POST":
        print("✅ Received FormData:", request.POST)
        print("✅ Received Files:", request.FILES)
        title = request.POST.get("songname")
        movie = request.POST.get("moviename")
        artists = request.POST.get("artistname")
        id_number = request.POST.get("songid")
        
        track = request.FILES.get("trackfile")
        image = request.FILES.get("picturefile")

        print(f"✅ Extracted Data: Title: {title} ID : {id_number} Artists: {artists}, Movie: {movie}")
        print(f"✅ Track: {track}, Image: {image}")

        if not title or not artists or not movie or not track or not image:
            print("❌ Missing fields in the request!")
            return JsonResponse({"error": "Missing fields"}, status=400)

        SongInfos = SongInformation.objects.create(
            Title=title,
            Id_number=id_number,
            Artists=artists,
            Movie=movie,
            Track=track,
            Picture=image
        )
        SongInfos.save()
        print("✅ Song saved successfully:", SongInfos.id)
        return JsonResponse({"message": "Song added successfully!", "id": SongInfos.id}, status=201)

    return JsonResponse({"Success": " Uploaded successfully!"}, status=201)

def getSongInfos(request):
    songs = SongInformation.objects.all()
    
    song_list = []
    for song in songs:
        song_list.append({
            "id": song.id,
            "Title": song.Title,
            "ID_Number": song.Id_number,
            "Artists": song.Artists,
            "Movie": song.Movie,
            "Track": request.build_absolute_uri(song.Track.url),
            "Picture": request.build_absolute_uri(song.Picture.url),
        })
    
    # Include total song count in the response
    response_data = {
        "total_songs": songs.count(),
        "songs": song_list
    }
    return JsonResponse(response_data, safe=False)


# Album

# @api_view(["GET", "POST"])
# @csrf_exempt
# def getAlbum(request):
#     if request.method == "POST":
#         # Extract data from request
#         albname = request.POST.get('albumname')
#         albmovie = request.POST.get('amoviename')
#         albartist = request.POST.get('albartistname')
#         albimage = request.FILES.get('albpicfile')
#         albtrack_ids = request.POST.getlist('albtrackfile')  # Get list of track IDs

#         print(f"Extracted Data: Album Name: {albname}, Movie: {albmovie}, Artist: {albartist}, Image: {albimage}, Tracks: {albtrack_ids}")

#         if not albname or not albmovie or not albartist or not albimage or not albtrack_ids:
#             print("❌ Missing fields in the request!")
#             return JsonResponse({"error": "Missing fields"}, status=400)

#         # ✅ Create Album Entry
#         album_info = AlbumInformation.objects.create(
#             Title=albname,
#             Artists=albartist,
#             Movie=albmovie,
#             Image=albimage
#         )

#         # ✅ Assign Many-to-Many Tracks
#         tracks = TrackModel.objects.filter(id__in=albtrack_ids)  # Get tracks from DB
#         album_info.Tracks.set(tracks)  # Assign track relationships
#         album_info.save()

#         print("✅ Album saved successfully:", album_info.id)
#         return JsonResponse({"message": "Album added successfully!", "id": album_info.id}, status=201)

#     return JsonResponse({"error": "Invalid request method"}, status=405)



# def getAlbumInfo(request):
#     if request.method == "GET":
#         albums = AlbumInformation.objects.prefetch_related('Tracks').all()
#         total_albums = albums.count()
        
#         album_list = []
#         for album in albums:
#             track_list = [
#                 {"id": track.id, "title": track.title, "url": track.url} for track in album.Tracks.all()
#             ]
#             album_list.append({
#                 "id": album.id,
#                 "Title": album.Title,
#                 "Artists": album.Artists,
#                 "Movie": album.Movie,
#                 "Image": album.Image.url if album.Image else None,
#                 "Alb_tracks": track_list
#             })

#         response_data = {
#             "total_Albums": total_albums,
#             "artists": [album.Artists for album in albums],
#             "Alb_tracks": album_list
#         }

#         return JsonResponse(response_data, safe=False, status=200)

#     return JsonResponse({"error": "Invalid request method"}, status=405)

#  Artists

@api_view(["GET", "POST"])
@csrf_exempt
def getArtists(request):
    if request.method == "POST":
        name = request.POST.get('artistname')
        genre = request.POST.get('genrename')
        id_number = request.POST.get('artistid')
        image = request.FILES.get('artistimage')
        print(f"Extracted Data ID: {id_number} Name: {name}, Genre: {genre}, Image: {image}")

        if not id_number or not name or not genre or not image:
            print("❌ Missing fields in the request!")
            return JsonResponse({"error": "Missing fields"}, status=400)
        print("Sucessfull")
        AristsInfo = ArtistInformation.objects.create(
           Name = name,
           Genres = genre,
           Image = image,
           Id_number = id_number
        )
        AristsInfo.save()
        print("✅ Song saved successfully:", AristsInfo.id)
        return JsonResponse({"message": "Artists Info added successfully!", "id": AristsInfo.id}, status=201)

    return JsonResponse({"Success": " Uploaded successfully!"}, status=201)
    return JsonResponse({"Success": " Uploaded successfully!"}, status=4005)

def getArtistInfos(request):
    Artists = ArtistInformation.objects.all()
    
    artist_list = []
    for artist in Artists:
        artist_list.append({
            "id": artist.id,
            "ID_number": artist.Id_number,
            "Name": artist.Name,
            "Genre": artist.Genres,
            "Image": request.build_absolute_uri(artist.Image.url),
        })
    
    # Include total song count in the response
    response_data = {
        "total_artists": Artists.count(),
        "artists": artist_list
    }
    return JsonResponse(response_data, safe=False)



#  Movie
@api_view(["GET", "POST"])
@csrf_exempt
def getmovie(request):
    if request.method == "POST":
        moviename = request.POST.get('Moviename')
        movieimage = request.FILES.get('Mimagefile')
        id_number = request.POST.get('Movieid')

        print(f"Extracted Data Movie Name: {moviename} Movie image: {movieimage} Id_Number: {id_number}")

        if not moviename or not movieimage:
            print("❌ Missing fields in the request!")
            return JsonResponse({"error": "Missing fields"}, status=400)
        print("Sucessfull")
        MovieInfo = MovieInformation.objects.create(
            Name = moviename,
            Image = movieimage,
            Id_number = id_number
        )
        MovieInfo.save()
        print("✅ Song saved successfully:", MovieInfo.id)
        return JsonResponse({"message": "Artists Info added successfully!", "id": MovieInfo.id}, status=201)

    return JsonResponse({"Success": " Executed successfully!"}, status=201)
    return JsonResponse({"Success": " Executed successfully!"}, status=4005)


def getMovieInfo(request):
    Movie = MovieInformation.objects.all()
    movie_list = []

    for movie in Movie:
        movie_list.append({
            "id": movie.id,
            "Movie_Name": movie.Name,
            "Image": request.build_absolute_uri(movie.Image.url),
            "ID_Number": movie.Id_number
        })
    
    # Include total song count in the response
    response_data = {
        "total_Movies": Movie.count(),
        "Movies": movie_list,
    }
    return JsonResponse(response_data, safe=False)




# Edit
@csrf_exempt
def update_artists(request, artist_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            artist = ArtistInformation.objects.get(id=artist_id)

            artist.Name = data.get("Name", artist.Name)
            artist.Id_number = data.get("Id_number", artist.Id_number)
            artist.Genres = data.get("Genres", artist.Genres)
            
            artist.save()
            return JsonResponse({"message": "Artist updated successfully!"})
        except ArtistInformation.DoesNotExist:
            return JsonResponse({"error": "Artist not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def delete_artist(request, artist_id):
    if request.method == 'DELETE':
        try:
            artist = ArtistInformation.objects.get(id=artist_id)
            artist.delete()
            return JsonResponse({"message":"Artist deleted successfully!"})
        except ArtistInformation.DoesNotExist:
            return JsonResponse({"error":"Artist not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)

# Delete Movie

@csrf_exempt
def delete_movie(request, movie_id):
    if request.method == 'DELETE':
        try:
            movie = MovieInformation.objects.get(id=movie_id)
            movie.delete()
            return JsonResponse({"message":"Movie deleted successfully!"})
        except MovieInformation.DoesNotExist:
            return JsonResponse({"error":"Movie not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)



@csrf_exempt
def delete_song(request, song_id):
    if request.method == "DELETE":
        try:
            song = SongInformation.objects.get(id=song_id)
            song.delete()
            return JsonResponse({"message": "Artist deleted successfully!"})
        except SongInformation.DoesNotExist:
            return JsonResponse({"error": "Artist not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)
