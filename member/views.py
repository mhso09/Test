from django.db.models.fields import DateTimeField
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from member.models import Member
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime
# Create your views here.
def member_register(request):
    return render(request, "member_register.html",{})

@csrf_exempt
def member_idcheck(request): # 아이디 중복체크하기
    context = {}

    memberid = request.GET['member_id']

    rs = Member.objects.filter(member_id=memberid)
    if (len(rs)) > 0 :
        context['flag'] = '1'
        context['result_msg'] = '중복'
    else:
        context['flag'] = '0'
        context['result_msg'] = '가능'

    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def member_insert(request): #가입시키기
    context = {}

    memberid = request.GET['member_id']
    memberpwd = request.GET['member_pwd']
    membername = request.GET['member_name']
    memberemail = request.GET['member_email']

    rs = Member.objects.create(member_id=memberid, member_pwd=memberpwd, member_email=memberemail, 
    member_name=membername, usage_flag='1', register_date=datetime.now())
    context['result_msg'] = "가입 성공 !! 홈에서 로그인 하세요"

    return JsonResponse(context, content_type="application/json")
