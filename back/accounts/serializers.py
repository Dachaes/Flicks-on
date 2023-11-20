from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.conf import settings
from allauth.account.adapter import get_adapter
from rest_framework import  serializers
from .models import User
import os
import tempfile


UserModel = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
    )
    age=serializers.IntegerField(required=False)
    img=serializers.ImageField(use_url=True, required=False)


    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'email': self.validated_data.get('email', ''),
            'age': self.validated_data.get('age', ''),
            'img': self.validated_data.get('img', ''),
        }
    

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)

        # 이미지 파일이 업로드되었으면 MEDIA_ROOT 디렉토리에 저장합니다.
        if self.cleaned_data['img']:
            image = self.cleaned_data['img']
            image_name = f'{user.pk}.jpg'
            image_path = os.path.join(settings.MEDIA_ROOT, image_name)

            # 이미지 파일을 MEDIA_ROOT 디렉토리에 저장합니다.
            with open(image_path, 'wb') as f:
                f.write(image.read())

            # 이미지 경로를 user.image 필드에 설정합니다.
            user.image = image_path
            user.save()

        return user




class CustomUserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    @staticmethod
    def validate_username(username):
        if 'allauth.account' not in settings.INSTALLED_APPS:
            # We don't need to call the all-auth
            # username validator unless its installed
            return username

        from allauth.account.adapter import get_adapter
        username = get_adapter().clean_username(username)
        return username

    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)