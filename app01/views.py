from django.shortcuts import render,HttpResponse
from app01.models import ClassInfo

# Create your views here.

def open(request):
    return render(request,'open.html')

def add(request):
    ClassInfo.objects.create(name='zhao', classes='人工智能23201', gender='男')
    return HttpResponse('添加成功')

def delete(request):
    ClassInfo.objects.filter(name='zhao').delete()
    return HttpResponse('删除成功')

def change(request):
    ClassInfo.objects.all().update(gender='女')
    return HttpResponse('修改成功')

def check(request):
    user_list = ClassInfo.objects.all()
    print(user_list)
    for obj in user_list:
        print(obj.name)
        print(obj.classes)
        print(obj.gender)
    return HttpResponse('查询成功')


