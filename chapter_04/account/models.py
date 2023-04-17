from django.db import models


# Create your models here.


class Account(models.Model):
    user_name = models.CharField(max_length=64, unique=True, null=False)
    user_email = models.EmailField(max_length=128, unique=True, null=False)
    password = models.CharField(max_length=64, null=False)
    signup_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "account"
