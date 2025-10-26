from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01.models import User
from app01.models import UserInfo


# Create your views here.

def index(request):
    return HttpResponse('成都东软学院')

def news(request):
    return render(request,"news.html")

def user(request):
    name='0'
    user=['zhao','qian','sun','li']
    return render(request,"user.html",{"n1":name,'n2':user})

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    username=request.POST.get('name')
    password=request.POST.get('password')
    user_list=UserInfo.objects.all()
    for obj in user_list:
        if obj.name == username:
            if obj.password==password:
                return redirect('https://nsu.edu.cn/')
            return render(request,'login.html',{'error_msg':'密码错误'})
        return render(request,'login.html',{'error_msg':'用户名不存在'})


def orm(request):
    UserInfo.objects.create(name='zhao',password='123',age=2)
    UserInfo.objects.create(name='qian',password='123',age=3)
    UserInfo.objects.create(name='sun',password='123',age=4)
    UserInfo.objects.create(name='li',password='123',age=5)
    return HttpResponse("操作成功")


def add(request):
    if request.method=='GET':
        return render(request,'user_add.html')
    name=request.POST.get('name')
    password=request.POST.get('pwd')
    age=request.POST.get('age')
    UserInfo.objects.create(name=name,age=age,password=password)
    return redirect('/list/')

def list(request):
    user_list=UserInfo.objects.all()
    return render(request,'user_list.html',{'user_list':user_list})

def delete(request):
    nid=request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/list/')
























from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from app01.utils.form import UserForm
from app01.models import User


def register(request):
    if request.method == 'POST':
        # 处理表单提交
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # 密码加密存储
            user = form.save(commit=False)
            user.upass = make_password(form.cleaned_data['upass'])
            user.save()
            # 注册成功，跳转至成功页面或登录页
            return redirect('register_success')
    else:
        # 初始化表单
        form = UserForm()

    return render(request, 'register.html', {'form': form})


def check_username(request):
    """AJAX 异步检查用户名是否已存在"""
    uname = request.GET.get('uname', '')
    exists = User.objects.filter(uname=uname).exists()
    # 返回 JSON 响应
    return JsonResponse({'exists': exists})


def register_success(request):
    """注册成功提示页"""
    return render(request, 'success.html')