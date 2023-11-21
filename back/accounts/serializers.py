from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.conf import settings
from allauth.account.adapter import get_adapter
from rest_framework import serializers
from movies.serializers import UserGenreSerializer


UserModel = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
    )
    age=serializers.IntegerField(required=False)


    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'email': self.validated_data.get('email', ''),
            'age': self.validated_data.get('age', ''),
        }
    

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user




class CustomUserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    usergenre_set = UserGenreSerializer(read_only=True, many=True)

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
        if hasattr(UserModel, 'last_login'):
            extra_fields.append('last_login')
        if hasattr(UserModel, 'date_joined'):
            extra_fields.append('date_joined')
        model = UserModel
        fields = ('pk', 'usergenre_set', *extra_fields,)
        # read_only_fields = ('email',)