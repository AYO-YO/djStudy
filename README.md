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
│       └── 存放插件（bootst）
```

