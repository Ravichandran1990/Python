from rest_framework import serializers
from .models import Song, Artist


class SongSerializer(serializers.ModelSerializer):   
    class Meta:
      model = Song
      fields = ('id', 'name', 'artist')
      
class ArtistSerializer(serializers.ModelSerializer):
  songs = SongSerializer(many=True)

  def create(self, validated_data):
    songs_data = validated_data.pop("songs")    
    artist = Artist.objects.create(**validated_data)
    for song_data in songs_data:
        print(song_data)
        Song.objects.create(artist=artist, **song_data)
    return artist
   
  class Meta:
    model = Artist
    fields = ('id', 'name', 'songs')