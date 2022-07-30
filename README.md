# Django3 学习笔记

[toc]

## APP

大项目进行功能划分，类似于Flaks蓝图

- 项目
  - app，用户管理
    - 表结构
    - 函数
    - HTML模板、CSS
  - app，订单管理
    - …相互独立，互不影响
  - app，后台管理
  - app，API
  - …
- 开发比较简洁，用不到多APP，一般情况下，项目下创建一个app

创建app命令：

```bash
python manage.py startapp app_name
```



文件结构

```
├── djStudy
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── settings.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py				【URL->函数】
│   └── wsgi.py
├── manage.py
├── README.md
├── templates
└── test_app
    ├── admin.py			【Django默认提供了admin后台管理，一般不用动】
    ├── apps.py				【固定，不用动，app启动类】
    ├── __init__.py
    ├── migrations			【一般不用动，数据库修改记录目录】
    │   └── __init__.py
    ├── models.py			【*重要，使用ORM对数据库进行操作】
    ├── tests.py			【单元测试】
    └── views.py			【*重要，函数】
```

## 快速上手

- 确保APP已注册

  - /setting.py，包名.文件名.类名

    ![image-20220723215431847](https://img.2fanbaby.cn/img/202207232154951.png)

- 编辑URL和视图函数对应关系，`/urls.py`

  url -> 函数

  ![image-20220724150755898](https://img.2fanbaby.cn/img/202207241508995.png)

- 编写视图函数

  ```python
  def index(request):
      return HttpResponse("welcome!")
  ```

- 启动Django项目

  ```bash
  python manage.py runserver
  ```

  Pycharm一键启动

## 编写一个页面

### templates

```python
return render(request, "html_remplate")
```

### 静态文件

```text
├── static
│   ├── css
│   │   └── 存放css
│   ├── img
│   │   └── 存放图片
│   ├── js
│   │   └── 存放js
│   └── plugins
│       └── 存放插件（bootstrap）
```

## 请求和响应

请求时Django比Flask多了一个crsf的校验。表单的中的请求应在表单最上层加入

```django
{% crsf_token %}
```



## 连接MySQL

首先安装pymysql

```bash
conda install pymysql
```

在`settings.py`中配置`DATABASE`，

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'testdb',
        'PASSWORD': 'zcx123',
        'HOST': '172.26.145.68',
    }
}
```

在`project`包下的`__init.py__`中初始化`pymysql`

```python
# coding=utf-8
import pymysql

pymysql.install_as_MySQLdb()
```

执行命令，完成初始化：

```bash
python manage.py migrate
```

### 创建模型

在`app`的`models.py`中，创建类名，即为表名，在类中创建的变量值即为字段名。

> models.py
>
> ```python
> # Create your models here.
> class User(models.Model):
>     """用户模型"""
>     # 用户名
>     username = models.CharField("用户名", max_length=50, unique=True, null=False)
>     # 密码
>     pwd = models.CharField("密码", max_length=100, null=False)
>     # 邮箱
>     email = models.CharField("邮箱", max_length=100, null=False)
>     # 0为超级管理员，1为普通用户
>     role = models.IntegerField("角色", default=1)
>     # 激活状态
>     is_active = models.BooleanField("用户是否激活", default=False)
>     # 注册时间
>     reg_time = models.DateTimeField("用户注册时间", auto_now_add=True)
> ```

### 激活模型

```bash
python manage.py makemigrations [app_name]
```

通过运行 `makemigrations` 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 *迁移*。

迁移是 Django 对于模型定义（也就是你的数据库结构）的变化的储存形式 - 它们其实也只是一些你磁盘上的文件。如果你需要的话，你可以阅读一下你模型的迁移数据，它被储存在 `app_name/migrations/0001_initial.py` 里。



执行`sqlmigrate [app_name] [迁移文件头]`可以展示将要执行的SQL语句。

```bash
python .\manage.py sqlmigrate test_app 0001
```



执行`migrate`，在数据库中完成创建。

```python
python manage.py migrate
```



数据库中创建一个特殊的表 `django_migrations` 来跟踪执行过哪些迁移。



### 更改模型

- 编辑 `models.py` 文件，改变模型。
- 运行 [`python manage.py makemigrations`](https://docs.djangoproject.com/zh-hans/4.0/ref/django-admin/#django-admin-makemigrations) 为模型的改变生成迁移文件。
- 运行 [`python manage.py migrate`](https://docs.djangoproject.com/zh-hans/4.0/ref/django-admin/#django-admin-migrate) 来应用数据库迁移。

### 数据库API

```pycon
In [3]: from test_app.models import User
# 获取所有字段
In [3]: User.objects.all()
Out[4]: <QuerySet []>

# 根据条件过滤，filter中的__相当于.
In [20]: User.objects.filter(reg_time__year=2022)
Out[20]: <QuerySet [<User: 1:admin>, <User: 2:gyf>]>

# 判断是否存在
In [5]: User.objects.filter(id=0).exists()

# 获取单个字段，返回列表，使用first()返回第一个值
# filter取不到值不会报错
In [5]: user = User.objects.filter(id=1).first()

# 创建一个字段
In [6]: user = User(username="admin",pwd="admin",email="zhaochunxu01828@os-easy.com",role=0)
In [7]: user.save()

# 查询字段内容
In [8]: user.id
Out[8]: 1

In [12]: user.reg_time
Out[12]: datetime.datetime(2022, 7, 25, 11, 24, 4, 433579)

# 修改字段， 修改单个字段使用save()，多个用户修改则使用update
In [36]: user.email = "1658432193@qq.com"
In [37]: user.save()
In [38]: user.email
Out[38]: '1658432193@qq.com'

# 批量修改字段
In [9]:users.update(is_active=True)
Out[9]: 2

# 获取结果QuerySet数量
In[10]: users.count()
Out[10]: 2
```
