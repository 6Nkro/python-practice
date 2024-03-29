# Generated by Django 4.2 on 2023-04-13 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64, verbose_name='사용자명')),
                ('user_email', models.EmailField(default='example@example.com', max_length=128, verbose_name='사용자이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registered_at', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'user',
            },
        ),
    ]
