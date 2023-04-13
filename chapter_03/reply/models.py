from django.db import models
from board.models import Board
from user.models import User


# Create your models here.

class Reply(models.Model):
    content = models.TextField(verbose_name='댓글 내용')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='게시글')
    write_date = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'comment'
        verbose_name = '댓글'
        verbose_name_plural = '댓글'
