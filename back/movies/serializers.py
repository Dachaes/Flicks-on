from rest_framework import serializers
from .models import Movie, Genre, Comment, UserGenre, UserImage
from accounts.models import User


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class UserNicknameSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('nickname', )

    users = UserNicknameSerializer(read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'movie',)


class MovieDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = '__all__'


class UserGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGenre
        exclude = ('id', 'user',)