from django.db import models


# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=64,
                                 verbose_name="이름",
                                 unique=True,
                                 null=False)

    user_email = models.EmailField(max_length=128,
                                   verbose_name='이메일',
                                   unique=True,
                                   null=False)

    password = models.CharField(max_length=64,
                                verbose_name="비밀번호",
                                null=False)

    registered_at = models.DateTimeField(auto_now_add=True,
                                         verbose_name="등록일자")

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
