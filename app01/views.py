from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01.models import UserInfo,Department



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

def layout(request):
    return render(request,'layout.html')

def depart_list(request):
    depart_list=Department.objects.all()
    return render(request,'depart_list.html',{'depart_list':depart_list})

def depart_add(request):
    if request.method=='GET':
        return render(request,'depart_add.html')
    title=request.POST.get('title')
    Department.objects.create(title=title)
    return redirect('/depart/list')

def depart_del(request):
    nid=request.GET.get('nid')
    Department.objects.filter(id=nid).delete()
    return redirect('/depart/list')

def depart_edit(request,nid):
    if request.method=='GET':
        depart=Department.objects.filter(id=nid).first()
        return render(request,'depart_edit.html',{'depart':depart})
    title=request.POST.get('title')
    Department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/list')

def user_list(request):
    user_list=UserInfo.objects.all()
    return render(request,'user_list.html',{'user_list':user_list})

def user_add(request):
    if request.method=='GET':
        context={
            'gender_choices':UserInfo.gender_choice,
            'depart_list':Department.objects.all()
        }
        return render(request,'user_add.html',context)

class MyForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs={'class':'form-control'}
    def clean_password(self,*args,**kwargs):
        password=self.cleaned_data.get('password')
        if len(password)<8:
            raise forms.ValidationError('密码长度必须大于8')
        return password

def user_modelform_add(request):
    if request.method == "GET":
        form = MyForm()
        return render(request, 'user_modelform_add.html',{"form":form})
    form=MyForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    return render(request,'user_modelform_add.html',{"form":form})

# def user_edit(request,nid):
#     if request.method=='GET':
#         depart=UserInfo.objects.filter(id=nid).first()
#         return render(request,'user_edit.html',{'depart':depart})
#     title=request.POST.get('title')
#     Department.objects.filter(id=nid).update(title=title)
#     return redirect('/depart/list')