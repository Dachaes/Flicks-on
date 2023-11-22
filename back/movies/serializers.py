from rest_framework import serializers
from .models import Movie, Genre, Comment, UserGenre, UserImage
from accounts.models import User


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content',)


class MovieDetailSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        class UserNicknameSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('id', 'nickname', )

        user_set = UserNicknameSerializer(read_only=True)
        user_nickname = serializers.CharField(source='user.nickname', read_only=True)
        user_id = serializers.IntegerField(source='user.id', read_only=True)
        class Meta:
            model = Comment
            fields = ('id', 'content', 'user_nickname', 'user_id', 'user_set', 'created_at', 'updated_at',)
            read_only_fields = ('created_at', 'updated_at')

    comment_set = CommentSerializer(read_only=True, many=True)
    release_date = serializers.CharField(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('release_date', )


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