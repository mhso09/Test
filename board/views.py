from django.http import response
from django.shortcuts import redirect, render
from board.models import Board
from django.db.models.base import ObjectDoesNotExist
# Create your views here.

def board(request):
    return render(request, 'board.html')

def pan(request): 
    rsBoard = Board.objects.all()
    
    return render(request, 'board_list.html', {
        'rsBoard':rsBoard
        })

def pan_write(request):
    return render(request, 'pan_write.html')

def pan_insert(request): 
    bitile = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    if bitile != "":
        rows = Board.objects.create(b_title=bitile, b_note=bnote, b_writer=bwriter)
        return redirect('/pan')
    else:
        return redirect('/pan_write')

def pan_view(request): # 내용 보기
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)
    return render(request, "pan_view.html", {
        'rsDetail': rsDetail
    })

def pan_edit(request):  # 수정하기
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)
    return render(request, "pan_edit.html", {
        'rsDetail': rsDetail
    })

def pan_update(request): #업데이트
    bno = request.GET["b_no"]
    btitle = request.GET["b_title"]
    bnote = request.GET["b_note"]

    try:
        board = Board.objects.get(b_no=bno)
        if btitle != "":
            board.b_title = btitle
        if bnote != "":
            board.b_note = bnote

        try:
            board.save()
            return redirect('/pan')
        except ValueError :
            return response({"success": False, "msg": "error발생."})
    
    except ObjectDoesNotExist:
        return response({"success": False, "msg": "게시글 없음"})

def pan_delete(request): # 삭제하기
    bno = request.GET['b_no']
    rows = Board.objects.get(b_no=bno).delete()

    return redirect('/pan')
