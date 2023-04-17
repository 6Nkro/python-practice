from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    queryset = Account.objects.all()

    user_name = serializers.CharField(
        validators=[UniqueValidator(queryset=queryset, message="이미 등록된 이름입니다.")])
    user_email = serializers.EmailField(
        validators=[UniqueValidator(queryset=queryset, message="이미 등록된 이메일입니다.")])

    class Meta:
        model = Account
        fields = ['user_name', 'user_email', 'password']
