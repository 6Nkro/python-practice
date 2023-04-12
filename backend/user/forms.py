from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    user_email = forms.CharField(
        error_messages={
            'required': '이메일를 입력해주세요.'
        },
        max_length=32, label="이메일")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        user_email = cleaned_data.get('user_email')
        password = cleaned_data.get('password')

        if user_email and password:
            try:
                user = User.objects.get(user_email=user_email)
            except User.DoesNotExist:
                self.add_error('user_email', '아이디가 없습니다')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다')
            else:
                self.user_id = user.id
