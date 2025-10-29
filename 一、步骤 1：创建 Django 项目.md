## 一、步骤 1：创建 Django 项目

Django 项目是所有 App 和配置的容器，通过 `django-admin` 命令创建。

### 1. 执行创建命令

打开终端，进入目标目录，执行：

```bash
# 格式：django-admin startproject 项目名
django-admin startproject project
```

### 2. 验证项目创建

进入项目根目录，启动开发服务器：

```bash
# 进入项目根目录
cd django1

# 启动开发服务器（默认端口 8000）
python manage.py runserver
# 若 8000 端口被占用，指定其他端口（如 8080）
# python manage.py runserver 8080
```

- 浏览器访问 `http://127.0.0.1:8000/`，看到 Django 欢迎页面即项目创建成功。

## 二、步骤 2：创建 Django App

Django 中 **App** 是功能模块的载体（如「用户模块」「博客模块」），一个项目可包含多个 App。

### 1. 执行创建命令

确保终端已激活虚拟环境，且处于项目根目录，执行：

```bash
# 格式：python manage.py startapp App名
python manage.py startapp app01
```

### 2. 注册 App 到项目

创建 App 后，必须在项目的 `settings.py` 中注册，否则 Django 无法识别该 App。

打开 `settings.py`，找到 `INSTALLED_APPS` 列表，添加 App 配置类：

```python
# my_django_project/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 新增：注册自定义 App（两种方式均可）
    'my_first_app',  # 方式 1：直接写 App 名
    # 'my_first_app.apps.MyFirstAppConfig',  # 方式 2：写 App 配置类路径（更规范）
]
```

## 三、创建视图函数

### 1.创建urls

```python
path('index/',views.index,name='index')
```

### 2.创建views.py

```python
def index(request):
    return HttpResponse('成都东软学院')
```

## 四、创建必备文件

![image-20250928132733427](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250928132733427.png)

## 五、在网页显示HTML

### 1.创建urls

```python
path('news/',views.news,name="news"),
```

### 2.创建views.py

```python
def news(request):
    return render(request,"news.html")
```

### 3.创建news.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<nav>
    <ul>
        <li>管理员账户</li>
        <li>用户管理</li>
        <li>IP管理</li>
    </ul>
</nav>
</body>
</html>
```

### 4.使用特殊语句

先在urls.py和views.py添加

```
path('user/',views.user,name="user"),
```



```
def user(request):
    name='0'
    user=['zhao','qian','sun','li']
    return render(request,"user.html",{"n1":name,'n2':user})
```

创建user.html

- 循环语句

```
{{n2.0}}

{% for item in n2 %}
<span>{{item}}</span>
{% endfor %}
```

- 字典

```
{{n3}}
{{n3.name}}
{% for item in n3.key %}
{% for item in n3.values %}
<ul>
	{% for k,v in n3.items %}
	<li>{{ k }}={{ v }}</li>
	{% endfor %}
</ul>
```

- 判断

```
{% if n1 == "lin" %}
	<h1>linlin</h1>
{% else %}
	<h1>nnono</h1>
{% endif %}
```

## 六、提交表单

- 响应，请求

```
request.method == 'POST'

note_id = request.GET.get('id')

file = request.FILES.get('note_file')

return render(request, 'note_detail.html', {'html_content': content})

return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')

return redirect('note_detail', note_id=note.id)
```

### 1.例

```
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    username=request.POST.get('name')
    password=request.POST.get('password')
    if username=='lin' and password=='123':
        return redirect('账号密码错误')
    return render(request,'login.html')
```

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户登录</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css">
    <style>
        /* 保持原有样式不变 */
        .account {
            width: 400px;
            border: 1px solid #dddddd;
            border-radius: 5px;
            box-shadow: 5px 5px 20px #aaa;
            margin: 100px auto 0;
            padding: 20px 40px;
        }

        .account h2 {
            margin-top: 10px;
            margin-bottom: 20px;
            text-align: center;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-control {
            display: block;
            width: 100%;
            height: calc(1.5em + .75rem + 2px);
            padding: .375rem .75rem;
            font-size: 1rem;
            font-weight: 400;
            line-height: 1.5;
            color: #495057;
            background-color: #fff;
            background-clip: padding-box;
            border: 1px solid #ced4da;
            border-radius: .25rem;
            transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
        }

        .remember-me {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
        }

        .remember-me input {
            margin-right: 8px;
            margin-top: 2px;
        }

        .btn-group {
            display: flex;
            justify-content: space-between;
            margin-bottom: 1rem;
        }

        .btn {
            display: inline-block;
            font-weight: 400;
            text-align: center;
            white-space: nowrap;
            vertical-align: middle;
            user-select: none;
            border: 1px solid transparent;
            padding: .375rem .75rem;
            font-size: 1rem;
            line-height: 1.5;
            border-radius: .25rem;
            transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
            cursor: pointer;
        }

        .btn-primary {
            color: #fff;
            background-color: #007bff;
            border-color: #007bff;
        }

        .btn-primary:hover {
            background-color: #0069d9;
            border-color: #0062cc;
        }

        .btn-secondary {
            color: #fff;
            background-color: #6c757d;
            border-color: #6c757d;
        }

        .btn-secondary:hover {
            background-color: #5a6268;
            border-color: #545b62;
        }

        .register-a-link {
            color: #007bff;
            text-decoration: none;
            background-color: transparent;
        }

        .register-a-link:hover {
            color: #0056b3;
            text-decoration: underline;
        }

        .right-align {
            text-align: right;
            display: block;
        }

        .error-message {
            color: red;
            margin-bottom: 1rem;
        }
    </style>
</head>
<body>
<div class="account">
    <h2>用户登录</h2>
    <form method="post" novalidate id="loginForm">
        {% csrf_token %}  <!-- 移到form标签内，这会自动生成正确的CSRF令牌 -->

        <div class="form-group">
            <label for="id_name">用户名</label>
            <input type="text" name="name" class="form-control" id="id_name" required>
            <span style="color:red;"></span>
        </div>

        <div class="form-group">
            <label for="id_password">密码</label>
            <input type="password" name="password" class="form-control" id="id_password" required>
            <span style="color:red;"></span>
        </div>

        <!-- 记住密码选项 -->
        <div class="remember-me">
            <input type="checkbox" name="remember" id="id_remember">
            <label for="id_remember">记住密码</label>
        </div>

        <!-- 错误提示 -->
        <div class="error-message" style="display:none;"></div>

        <!-- 登录和重置按钮组 -->
        <div class="btn-group">
            <input type="submit" value="登 录" class="btn btn-primary">{{ error_msg }}
            <input type="reset" value="重 置" class="btn btn-secondary">
        </div>

        <a href="/register/" class="register-a-link right-align">免费注册</a>
    </form>
</div>

<script>
    // 保持原有脚本不变
    document.getElementById('loginForm').addEventListener('submit', function(e) {
        const username = document.getElementById('id_name').value;
        const password = document.getElementById('id_password').value;
        const errorElement = document.querySelector('.error-message');

        if (!username || !password) {
            e.preventDefault();
            errorElement.textContent = '请输入用户名和密码';
            errorElement.style.display = 'block';
        } else {
            errorElement.style.display = 'none';
        }
    });

    document.querySelector('input[type="reset"]').addEventListener('click', function() {
        document.querySelector('.error-message').style.display = 'none';
    });
</script>
</body>
</html>

```

## 七、mysql

#### 7.1 安装

* 下载到django目录下

* 解压到当前文件夹


#### 7.2 创建配置文件

![image-20251011140029666](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20251011140029666.png)

#### 7.3 配置环境变量

![image-20251011140111962](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20251011140111962.png)

#### 7.4 初始化

* 以管理员身份打开cmd

* 输入初始化命令

  ```
  mysqld --initiakize-insecure
  ```

#### 7.5 启动MySQL

* 临时启动

  ```
  mysqld
  ```

* 制作成Windows服务，服务来进行关闭和进行

  * 制作服务

    ```
    mysqld --install mysql00
    ```

  * 启动和关闭服务

    ```
    >>> net start mysql00
    >>> net stop mysql00
    ```

#### 7.6 连接MySQL

```
mysql -u root -p
```

#### 7.7本课程常用操作

* show databases 查看所有数据库
* create database XXX DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
* ues XXX 进入数据库
* show tabel 查看所有表格
* select * from xxx 查看表格数据

#### 7.8 修改密码

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root123';
```

### 八、在django中使用MySQL

ORM框架

#### 8.1 安装第三方模块

```
python pip install mysqlclient
```

#### 8.2 ORM

- 创建、修改数据库中的表
- 操作表里的数据

#### 8.3 创建数据库

- 启动mysql

```
create database xxx DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

#### 8.4 Django连接数据库

在settings文件中进行配置修改

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django1',  # 数据库名字
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': '127.0.0.1',  # lockhost
        'PORT': 3306,
    }
}
```

#### 8.5 ORM操作表

- 创建表

```
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    age=models.IntegerField()
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```

- 表结构修改
  - 增加
  
    ```
    UserInfo.objects.create(name='zhao',password='123',age=2)
    ```
  
  - 删除
  
    ```
    UserInfo.objects.filter(id=2).delect()
    ```
  
  - 查询
  
    ```
    user_list=UserInfo.objects.all()
    print(user_list)
    for obj in user_list:
    	print(obj.name)
    user=UerInfo.objects.filter(id=17).first()
    ```
  
  - 修改
  
    ```
    UserInfo.objects.all().update(age=40)
    UserInfo.objects.filter(name='zhao').update(age=40)
    ```
  

#### 8.6案例

- 1.展示用户列表

  - 获取所有用户信息
  - 模板语法填入HTML
  - 返回给前端

  ```
  def user_list(request):
      data_list = UserInfo.objects.all()
      return render (request,'user_list.html',f'data_list':data_list})
  ```

- 2.添加用户

  - GET,看到页面，输入内容
  - POST,提交写入到数据库

  ```
  def user_add(request):
      if request.method == "GET":
      return render (request,'user_add.html')
      username = request.PosT.get("user")
      password = request.PosT.get("pwd")
      age = request.PoST.get("age")
      UserInfo.objects.create(name=username ,password=password,age=age)
      return redirect('/user/list')
  ```

- 3.删除用户

  ```
  http://127.0.0.1:8000/info/delete/?nid=1
  def user_del(request):
      nid = request.GET.get("nid")
      UserInfo.objects.filter (id=nid) .deleteO)
      return redirect('/user/list')
  ```

  

### 九、git-github

#### 1.创建远程仓库

![image-20251029132210970](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20251029132210970.png)

![image-20251029132313562](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20251029132313562.png)

注意是否出现.git文件夹

```
git init
```

![image-20251029132409131](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20251029132409131.png)

#### 2.添加文件到暂存区

先将本地文件添加到 Git 暂存区：

```
git add .  # 添加当前目录所有文件（注意空格和点）
# 或指定单个文件：git add 文件名
```

#### 3.添加文件到暂存区

将暂存区的文件提交到本地仓库，并添加提交信息：

```
git commit -m "首次提交：初始化项目"  # 引号内填写提交说明
```

#### 4.关联本地仓库与远程仓库

在本地终端执行，将本地仓库与 GitHub 远程仓库关联：

```
git remote add origin https://github.com/你的用户名/仓库名.git
# 若关联错误，可删除后重新关联：git remote rm origin
```

#### 5.推送到 GitHub 远程仓库

首次推送时，需要指定分支（默认主分支为 `main` 或 `master`，根据 GitHub 配置）

```
git push -u origin main  # 若分支是 master 则替换为 git push -u origin master
```

