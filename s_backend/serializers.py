from rest_framework import serializers
from .models import SongInformation

class SongDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongInformation
        fields = '__all__'

