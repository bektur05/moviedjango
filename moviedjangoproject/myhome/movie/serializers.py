from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name',]


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name',]


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieVideosSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class MovieMomentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ["movie_moments"]


class RatingSerializers(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    user = ProfileSimpleSerializers()

    class Meta:
        model = Rating
        fields = ['id', 'user', 'text', 'parent', 'start', 'created_date']


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class MovieListSerializers(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    genre = GenreSerializers(many=True)
    country = CountrySerializers(many=True)
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'movie_image', 'year', 'genre', 'country',
                  'status_movie', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class ActorDetailSerializers(serializers.ModelSerializer):
    actor_movies = MovieListSerializers(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ['actor_name', 'actor_image', 'bio', 'age', 'actor_movies']



class CountryDetailSerializers(serializers.ModelSerializer):
    movies = MovieListSerializers(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name', 'movies']


class HistorySerializers(serializers.ModelSerializer):
    user = ProfileSimpleSerializers()
    movie = MovieListSerializers()

    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']


class MovieDetailSerializers(serializers.ModelSerializer):
    year = serializers.DateField(format='%d-%m-%Y')
    genre = GenreSerializers(many=True)
    country = CountrySerializers(many=True)
    director = DirectorSerializers(many=True)
    actor = ActorSerializers(many=True)
    movies_videos = MovieVideosSerializers(many=True, read_only=True)
    movies_moments = MovieMomentsSerializers(many=True, read_only=True)
    ratings = RatingSerializers(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_image', 'movie_trailer', 'genre', 'types', 'director', 'actor', 'year',
                  'movie_time', 'description', 'status_movie', 'country', 'movies_moments', 'movies_videos', 'ratings']


