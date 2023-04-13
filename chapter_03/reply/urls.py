from django.urls import path
from . import views

urlpatterns = [
    path('write/<int:board_id>/', views.reply_write, name='reply_write'),
]