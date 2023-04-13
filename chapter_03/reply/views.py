from django.shortcuts import redirect
from django.http import JsonResponse
from board.models import Board
from .models import Reply
from user.models import User


# Create your views here.
def reply_write(request, board_id):
    user_id = request.session.get('user')
    if not user_id:
        return redirect('/user/login/')

    if request.method == 'POST':
        content = request.POST.get('content')
        writer = User.objects.get(pk=user_id)
        board = Board.objects.get(pk=board_id)
        reply = Reply(content=content, writer=writer, board=board)
        reply.save()
        return JsonResponse({'result': 'success'})
    return JsonResponse({'result': 'error'})
