import json
import os

from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers

from config.settings import base
from members.tasks import send_mail

from ..tokens import account_activation_token

User = get_user_model()


class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'birthday',
            'password',
            'create_date',
        )

    # password의 길이가 8글자 아래일 경우 에러발생
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("비밀번호는 8글자 이상이여야 합니다.")
        return value

    # 위의 validated의 값이 다 통과되고 password와 password_check의 값이 같으면
    # create_user로 user값 생성
    # create로 만들경우 해싱된 값이 아닌 user가 쓴 값이 그대로 들어감
    def create(self, validated_data):

        user = User.objects.create_user(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            birthday=self.validated_data['birthday'],
            password=self.validated_data['password']
        )
        user.save()
        send_mail.delay(user.pk)

        return validated_data
