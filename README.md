# MiniDjango

+ ### 在pycharm中安装虚拟环境

+ ### 在虚拟环境中创建Django应用

    + #### 1、这个应用有两部分组成：

        + *一个让人们查看和投票的公共站点*

        + *一个让您能添加、修改和删除投票的管理站点*

    + #### 2、创建项目

        + *django-admin startproject mysite*

        + startproject创建的目录结构

            + 

            ```python
            mysite/
                manage.py
                mysite/
                    __init__.py
                    settings.py
                    urls.py
                    wsgi.py
            ```

    + #### 3、启动服务器

        + 让我们来确认一下你的Django项目是否真的创建成功了，切到mysite目录下

        + ```python
            python manage.py runserver
            ```

        + 能看到如下输出就说明项目创建成功：

            + ​	

                ```python
                Performing system checks...
                
                System check identified no issues (0 silenced).
                
                You have unapplied migrations; your app may not work properly until they are applied.
                Run 'python manage.py migrate' to apply them.
                
                八月 01, 2018 - 15:50:53
                Django version 2.0, using settings 'mysite.settings'
                Starting development server at http://127.0.0.1:8000/
                Quit the server with CONTROL-C.
                ```

            + *你刚刚启动的是 Django 自带的用于开发的简易服务器，它是一个用纯 Python 写的轻量级的 Web 服务器。我们将这个服务器内置在 Django 中是为了让你能快速的开发出想要的东西，因为你不需要进行配置生产级别的服务器（比如 Apache）方面的工作，除非你已经准备好投入生产环境了*

        + 现在服务器正在运行，在浏览器访问http://127.0.0.1:8000.将会看到一个“祝贺”页面，随着一只火箭发射，服务器已经运行了

    + #### 4、创建投票应用

        + 现在开发这个“项目”环境已经配置好了，就可以开始干活了

        + 在Django中每一个应用都是一个Python包，并且遵循着形同的约定。Django自带一个工具，可以帮您生成应用的基础结构，这样你就能专心的写代码了，而不是创建目录

            + ##### 项目VS应用

            + 项目和应用有什么区别？

                + 1、应用是专门做某件事的网络应用程序--比如博客系统，或者公共记录的数据库，或者简单的投票程序。
                + 2、项目是一个网站使用的配置和应用的集合。
                + 3、项目可以包含多个应用，应用可以被多个项目使用。

        + ##### 我们将在manage.py同级目录下创建投票应用

            + ```python
                python manage.py startapp polls
                ```

            + polls的目录大致如下：

                + ```python
                    polls/
                        __init__.py
                        admin.py
                        apps.py
                        migrations/
                            __init__.py
                        models.py
                        tests.py
                        views.py
                    ```

            + *这个目录结构包含了投票应用的所有内容*

    + #### 5、编写第一个视图

        + 打开  polls/views.py

        + ```python
            from django.http import HttpResponse
            
            def index(reauest): 
                return HttpResponse("Hello, World. You're at the polls index.")
            ```

        + 这事Django中最简单的视图，如果想看效果，我们需要将一个URL映射到它

        + 这里我们需要URLConf

            + 为了创建URLConf，请在polls目录下新建一个urls.py

            + 这样得到了如下应用目录：

            + ```python
                polls/
                    __init__.py
                    admin.py
                    apps.py
                    migrations/
                        __init__.py
                    models.py
                    tests.py
                    urls.py
                    views.py
                ```

        + 在polls/urls.py中，输入如下代码：

        + ```python
            from django.urls import path
            
            from . import views
            
            urlpatterns = [
                path("", views.index, name-"index")
            ]
            ```

        + 下面是要在根URLconf 文件中指定我们创建的polls.urls模块

        + 在mysite/urls.py 文件的urlpatterns列表中插入一个include() , 如下：

        + 

        ```python
        from django.contrib import admin
        from django.urls import include, path
        
        urlpatterns = [
            path("polls/", include("polls.urls")),
            path("admin/", admin.site.urls),
        ]
        ```

        + 函数include()允许应用其他URLconf

        + 每当Django遇到：func：*~django.urls.include*时，它会截断此项匹配的URL的部分，并将剩余的字符串发送到URLconf以供进一步处理。

            + **我们设计 [`include()`](https://docs.djangoproject.com/zh-hans/2.0/ref/urls/#django.urls.include) 的理念是使其可以即插即用。因为投票应用有它自己的 URLconf( `polls/urls.py` )，他们能够被放在 "/polls/" ， "/fun_polls/" ，"/content/polls/"，或者其他任何路径下，这个应用都能够正常工作。**

        + 把index视图加进URLconf中，就可以验证是否正常工作

        + 运行如下代码：

            ```python
            python manage.py runserver
            ```

            用浏览器访问http://localhost:8000/polls/,

            就会看到 “**Hello， World. You're at the polls index**.”

        + **函数path()**

        + 具有四个参数，两个必须参数： *route和 view* ， 两个可选参数：*kwargs 和 name*

            + route

                + route是一个匹配URL的准则（类似正则表达式）。当Django响应一个请求时，他会从urlpatterns的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。

            + view

                + 当Django找到一个匹配的准则，就会调用这个特定的视图函数，并传入一个HttpResponse对象作为第一个参数

            + kwargs

                + 任意关键字参数可以作为一个字典传递目标视图函数

            + name

                + 为您的URL取名能使你在Django的任意地方应用它，尤其是在模板中，

                + 这个特性允许你只改一个文件就能全局的修改某个URL模式

    + #### 6、数据库配置

        + 现在，打开mysite/settings.py,这是个包含Django项目设置的Python模块

        + 通常这个配置文件中使用SQLite作为默认数据库

        + 如果想使用其他的数据库，就需要安装合适的引擎，然后在设置文件中*DATABASE"default"*项目中的一些键值：

            + **ENGINE-- 可选值有**：

                + "django.db.backends.sqlite3","django.db.backends.postgresql",
                + "django.db.backends.oracle","django.db.backends.mysql"

            + **NAME** -- 数据库名称 

                + 默认值**os.path.join**(**BASE_DIR**, "**db.sqlite3**")
                + 将会把数据库文件存储到项目的根目录

            + 如果不使用SQLite，则必须添加一些额外设置，比如：**USER**、 **PASSWORD**、 **HOST**

            + 想了解更多数据库设置方面的内容，**请看文档**：

                [https://docs.djangoproject.com/zh-hans/2.0/ref/settings/#std:setting-DATABASES]: 

                + **SQLite 以外的其它数据库**

                    **如果你使用了 SQLite 以外的数据库，请确认在使用前已经创建了数据库。你可以通过在你的数据库交互式命令行中使用 "`CREATE DATABASE database_name;`" 命令来完成这件事。**

                    **另外，还要确保该数据库用户中提供 `mysite/settings.py` 具有 "create database" 权限。这使得自动创建的 [test database](https://docs.djangoproject.com/zh-hans/2.0/topics/testing/overview/#the-test-database) 能被以后的教程使用。**

                    **如果你使用 SQLite，那么你不需要在使用前做任何事——数据库会在需要的时候自动创建。**

        + 编辑***mysite/settings.py***之前，先设置**TIME_ZONE**为您自己的时区

        + 此外，关注一下文件头部的**INSTALLED_APPS**设置项。这里包含了项目中启用的所有的**Django**应用，应用能在多个项目中使用，你也可以打包并且发布应用，让别人使用它们。

            + 通常，**INSTALLED_APPS**默认包括了一下**Django**的自带应用：

                + **django.contrib.admin**                        -- 管理员站点，
                + **django.contrib.auth**                           -- 认证授权系统
                + **django.contrib.contenttypes**           -- 内容类型框架
                + **django.contrib.sessions**                     -- 会话框架
                + **django.contrib.messages**                   -- 消息框架
                + **django**.**contrib.staticfiles**                   -- 管理静态文件的框架

            + **这些应用被默认启用是为了给常规项目提供方便**

            + 默认开启的某些应用需要至少一个数据表，所以，在使用它们之前需要在数据库中创建一些表。

            + 请执行一下命令：

                + ```python
                    python manage.py migrate
                    ```

            + 这个migrate命令检查INSTALL_APPS设置，为其中的每个应用创建需要的数据表

                + **写给极简主义**
                    + **就像之前说的，为了方便大多数项目，我们默认激活了一些应用，但并不是每个人需要它们。如果你不需要某个或某些应用，你可以在运行migrate前毫无顾虑的从INSTALLED_APPS里注释或者删除他们。migrate命令只会在INSTALLED_APPS里声明了的应用进行数据库迁移。**

    + #### 7、创建模型

        + 在Django里写一个数据库的Web应用的第一步是定义模型

            + 也就是数据库结构设计和附加的其他元数据

            + **设计哲学**

                + 模型是真实数据简单明确的描述。它包含了储存的数据所必要的字段和行为。

                + Django遵循

                    [https://docs.djangoproject.com/zh-hans/2.0/misc/design-philosophies/#dry]: 

                + 它的目标是你只需要定义数据模型，然后其他的杂七杂八的代码你都不用担心，他们会自动从模型生成

        + 在这个简单的投票应用中，需要创建两个模型：

            + 问题 **Question**

            + 选项 **Choice**

            + 编辑polls/models.py

                + 

                    ```python
                    from django.db import models
                    
                    class Question(models.Model):
                        question_text = models.CharField(max_length)
                        pub_date = models.DateTimeField("date published")
                        
                    
                    class Choice(models.Model):
                        question = models.ForeignKey(Question, 			           				on_delete=models.CASCADE) 
                        choice_text = models.CharField(max_length)
                        votes = models.InterField(default=0)
                        
                    ```

                + 代码非常直白。每个模型被表示为django.db.models.Model类的子类

                + 每个模型有一些变量，它们都表示模型里一个数据库字段

                + 每个字段都是Field类的实例 - 比如

                    + 字符串被表示为CharField
                    + 日期时间字段被表示为DateTimeField
                    + 这将告诉Django每个字段要处理的数据类型
                    + 定义Field类实例需要参数，例如CharField需要一个max_length参数，这个参数的用处定义数据库结构，也用于验证数据
                    + Field也可以接受可选参数，在上面的例子中：我们将votes的default也就是默认值，设为0.
                    + 注意在最后，我们使用foreignKey定义了一个关系，这将告诉Django，每个Choice都关联到一个Question对象
                        + Django支持所有常用的数据库关系：
                        + 多对一、多对多和一对一

    + #### 8、激活模型

        + 上面的一小段用于创建模型的代码给Django框架很多信息，通过这些信息，Django可以：

            + 为这个应用创建数据库schema（生成**CREATE TABLE**语句）
            + 创建可以与Question和Choice对象进行交互的Python数据库API

        + 首先把polls应用安装到我们的项目里   

            + **设计哲学**   

                + *Django应用是“可拔插”的。你可以在多个项目中使用同一个应用，初此之外，你还可以发布自己的应用，因为他们并不会被绑定到当前的Django上。*

            + 为了在我们的工程中包含这个应用，我们需要在配置类INSTALLED_APPS中添加设置

            + 因为**PollsConfig**类写在文件**polls/apps.py**中，所以它的点式路径是“**polls.apps.PollsConfig**”

                + 在文件mysite/settings.py中INSTALLED_APPS子项添加点式路径：

                + ```python
                    INSTALLED_APPS = [
                        'polls.apps.PollsConfig',
                        'django.contrib.admin',
                        'django.contrib.auth',
                        'django.contrib.contenttypes',
                        'django.contrib.sessions',
                        'django.contrib.messages',
                        'django.contrib.staticfiles',
                    ]
                    ```

        + 现在你的Django项目会包含polls应用，接着运行下面的命令：

            + ```python
                python manage.py makemigrations polls
                ```

            + 你将会看到类似下面这样的输出：

                + ```python
                    Migrations for 'polls':
                      polls/migrations/0001_initial.py:
                        - Create model Choice
                        - Create model Question
                        - Add field question to choice
                    ```

            + 通过运行makemigrations命令，Django会检测你对模型文件的修改，并且把自修改的部分储存为一次迁移

            + 模型的迁移数据在**polls/migrations/0001_initial.py**里

        + Django有一个自动执行数据库迁移并同步管理你的数据库结构的命令-

            + 这个命令是migrate，我们马上会接触它  

            + 但是首先，让我们看看迁移命令执行那些SQL语句  

            + sqlmirate命令接收一个迁移的名称，然后返回对应的SQL：  

                + ```python
                    python manage.py sqlmigrate polls 0001
                    ```

            + 你将会看到类似下面这样的输出（我们把它重组成了人类可读的格式）：

                + ```python
                    BEGIN;
                    --
                    -- Create model Choice
                    --
                    CREATE TABLE "polls_choice" (
                        "id" serial NOT NULL PRIMARY KEY,
                        "choice_text" varchar(200) NOT NULL,
                        "votes" integer NOT NULL
                    );
                    --
                    -- Create model Question
                    --
                    CREATE TABLE "polls_question" (
                        "id" serial NOT NULL PRIMARY KEY,
                        "question_text" varchar(200) NOT NULL,
                        "pub_date" timestamp with time zone NOT NULL
                    );
                    --
                    -- Add field question to choice
                    --
                    ALTER TABLE "polls_choice" ADD COLUMN "question_id" integer NOT NULL;
                    ALTER TABLE "polls_choice" ALTER COLUMN "question_id" DROP DEFAULT;
                    CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");
                    ALTER TABLE "polls_choice"
                      ADD CONSTRAINT "polls_choice_question_id_246c99a640fbbd72_fk_polls_question_id"
                        FOREIGN KEY ("question_id")
                        REFERENCES "polls_question" ("id")
                        DEFERRABLE INITIALLY DEFERRED;
                    
                    COMMIT;
                    ```

            + 生成的SQL语句是为你所用的数据库定制的，所以那些和数据库有关的字段类型，比如auto_increment(MySQL)、serial（PostgreSQL）和integer primary key autoincrement(SQLite),Django会帮你自动处理。那些和引号相关的事情 -- 例如，是使用单引号还是使用双引号 - - 也一样被处理。

            + 这个sqlmigrate命令并没有真正在你的数据库中的执行迁移 - 它只是把命令输出到屏幕上，让您看看Django认为需要执行那些SQL语句。这在您想看看Django到底准备做什么，或者你是数据库管理员，需要些脚本来批量处理数据库时会很有用。

        +  如果你感兴趣，你也可以试试运行python manage.py check ,这个命令帮助检查项目中的问题，并且在检查过程中不会对数据库进行任何操作。

        + 现在，再次执行migrate命令，在数据库里创建新定义的模型的数据表：  

            + ```python
                python manage.py migrate
                ```

            + ```python
                Operations to perform:
                  Apply all migrations: admin, auth, contenttypes, polls, sessions
                Running migrations:
                  Rendering model states... DONE
                  Applying polls.0001_initial... OK
                ```

        +   这个migrate命令选中所有还没执行过的迁移（Django通过数据库中创建一个特殊的表django_migrations来跟踪执行过哪些迁移）并应用在数据库上 - 也就是将你对模型的更改同步到数据库的结构上。

        + 迁移的功能非常强大，它能让你在开发过程中持续的改变数据库结构而不需要重新删除和创建表 - 它专注于使数据据平滑升级而不会丢失数据。

        + 现在，我们只需要记住，改变模型需要三步：

            + 编辑models.py 文件，                                       --                    改变模型。
            + 运行python  manage.py makemigrations      --                    为模型的改变生成迁移文件
            + 运行python manage.py migrate                      --                    来应用数据库迁移

        + 数据库迁移被分解成生成和应用两个命令是为了你能够在代码控制系统上提交迁移数据并使用能在多个应用里使用过；

        + 这不仅仅会让开发更加简单，也给别的开发者和生产环境中的使用带来方便

            + 通过阅读文档：	

                [https://docs.djangoproject.com/zh-hans/2.0/ref/django-admin/]: 

            + 你可以获得关于manage.py工具的更多信息

    + #### 9、初试API

        + 现在我们进入交互式Python命令行，尝试一下Django为你创建的各种API

        + 通过一下命令打开Python命令行：

            + ```python
                python manage.py shell
                ```

        + 当你成功进入命令行，来试试database API吧！

            + [https://docs.djangoproject.com/zh-hans/2.0/topics/db/queries/]: 

        +  

            ```python
            >>> from polls.models import Choice, Question  # Import the model classes we just wrote.
            
            # No questions are in the system yet.
            >>> Question.objects.all()
            <QuerySet []>
            
            # Create a new Question.
            # Support for time zones is enabled in the default settings file, so
            # Django expects a datetime with tzinfo for pub_date. Use timezone.now()
            # instead of datetime.datetime.now() and it will do the right thing.
            >>> from django.utils import timezone
            >>> q = Question(question_text="What's new?", pub_date=timezone.now())
            
            # Save the object into the database. You have to call save() explicitly.
            >>> q.save()
            
            # Now it has an ID.
            >>> q.id
            1
            
            # Access model field values via Python attributes.
            >>> q.question_text
            "What's new?"
            >>> q.pub_date
            datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)
            
            # Change values by changing the attributes, then calling save().
            >>> q.question_text = "What's up?"
            >>> q.save()
            
            # objects.all() displays all the questions in the database.
            >>> Question.objects.all()
            <QuerySet [<Question: Question object (1)>]>
            ```

        + 给模型增加__str__()方法很重要，这不仅仅能给你在命令行里使用带来方便，Django自动生成的admin里也是用这个方法来表示对象。

            + ```python
                from django.db import models
                
                class Question(models.Model):
                    # ...
                    def __str__(self):
                        return self.question_text
                
                class Choice(models.Model):
                    # ...
                    def __str__(self):
                        return self.choice_text
                ```

+ ## 介绍Django管理界面

    + **设计哲学**
        + 为你的员工或客户生成一个用户添加，修改和删除内容的后台是一项缺乏创造性和乏味的工作。因此，Django全自动的根据模型创建后台界面。
        + Django产生于一个公众页面的内容发布者在完完全全分离的新闻类站点的开发过程中。站点管理人员使用管理系统来添加新闻、事件和体育时讯等，这些添加的内容被显示在公众页面上。Django通过为站点管理人员创建统一的内容编辑界面解决了这个问题。
        + 管理界面不是为了网站的访问者，而是为了管理者准备的。

    + #### 10、创建一个管理员账号

        + 命令

            + ```python
                python manage.py createsuperuser
                ```

        + 用户名：

            + ```python
                Username: admin
                ```

        + 邮件：

            + ```python
                Email address：admin@example.com
                ```

        + 密码：

            + ```python
                Password:*********
                Password(again):********
                Superuser created successfully.
                ```

    + #### 11、启动开发服务器

        + Django的管理界面默认就是启动的。让我们启动开发服务器，看看它到底是什么样的。

        + 如果未启动，用命令：

            + ```python
                python manage.py runserver
                ```

        + 现在打开浏览器，转到你本地域名的“/admin/”目录， -- 比如“http://127.0.0.1:8000/admin/”,会看见管理员登陆的界面：

        + ![1555054780513](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1555054780513.png)

    + #### 12、进入管理站点页面

        + ![1555054865367](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1555054865367.png)

    + #### 13、向管理页面中加入投票应用

        + 但是我们的投票应用在哪啊？它没在索引页面里显示。

        + 只需要做一件事：

            + 我们得告诉管理页面，问题Question对象要被管理。

            + 打开polls/admin.py文件，把它编辑成下面这样：

                + ```python
                    from django.contrib import admin
                    
                    from .models import Questioin
                    
                    admin.site.register(Question)
                    ```

    + #### 14、体验便捷的管理功能

        + 现在向管理页面注册了问题Question类，Django知道他应该被显示在索引页里：
        + ![1555055329283](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1555055329283.png)

    + #### 15、编写更多视图

        + ```python
            def detail(request, question_id):
                return HttpResponse("You're looking at question %s." % question_id)
            
            def results(request, question_id):
                response = "You're looking at the results of question %s."
                return HttpResponse(response % question_id)
            
            def vote(request, question_id):
                return HttpResponse("You're voting on question %s." % question_id)
            ```

        + 把这些新的视图添加进polls.urls模块中，只要添加几个url()函数调用就行：

            + 

                ```python
                from django.urls import path
                
                from . import views
                
                urlpatterns = [
                    # ex: /polls/
                    path('', views.index, name='index'),
                    # ex: /polls/5
                    path('<int:question_id>/', views.detail, name='detail'),
                    path('<int:question_id>/results/', views.results, 											name='results') 
                    path('<int:question_id>/vote/', views.vote, name='vote')
                ]
                
                ```

            + 然后你看看你的浏览器，如果跳转到“/polls/34/”,Django将会运行detail()方法并且展示你在url里提供的问题ID，再试试看看“/polls/34/vote/”

            + 当某人请求你的网站的某一页是，比如说，“/polls/34/”,Django将会载入mysite.urls模块，因为这在配置项ROOT_URLCONF中设置了，然后Django寻找名为urlpatterns变量并且按匹配正则表达式，在找到匹配项‘polls’，它切掉匹配的文本（“polls/”）,将剩余文本 -- “34/”,发送至“polls.urls.URLconf”做进一步处理，在这里剩余文本匹配了<int:question_id>/‘,是的我们Django以如下形式调用detail()

                + ```python
                    detail(request=<HttpRequest object>, question_id = 34)
                    ```

            + question_id = 34由<int:questin_id>匹配生成，使用见括号“捕获“这部分URL，且以关键字参数的形式发送给视图函数，上述字符串的：question_id部分定义了将用于区分匹配模式的变量名，而int：则是一个转换器决定了应该以什么变量类型匹配这部分的URL路径。

    + ####  16 、一个真正有用的视图

        + 每个视图必须含被请求页面内容的HttpResponse对象，或者抛出一个异常，比如Http404.

        + 你的视图可以从数据库里读取数据记录，可以使用一个引擎模板（比如Django自带的，或者其他第三方的），可以生成一个PDF文件，可以输出一个XML，创建一个ZIP文件，你可以做任何您想做的事，使用任何你想用的python库。

        + **Django要求返回一个HttpResponse，或者抛出一个异常**

        + 我们在index()函数中插入了一些新内容，让他能展示数据库里以发布日期排序的最近5个投票问题，以空格分割：

            + ```python
                from django.http import HttpResponse
                
                from . models import Qestion
                
                def index(request):
                    latest_question_list = Question.object.order_by('-												pub_date'[5])
                    output = ', '.join([q.question_text for q in 									latest_question_list])
                    return HttpResponse(output)
                ```

        + 这里有个问题：页面的设计写死在视图函数的代码里。如果你想改变页面的样子，你需要改变Python代码。所以让我们使用Django的模板系统，只要创建一个视图，就可以将页面的设计从设计代码中分离出来。

        + 首先，在你的polls下创建一个templates目录，Django将会从这个目录里查找模板文件。

        + 在你刚刚创建的templates目录里。在创建一个目录polls，然后在其中新建一个文件index.html。换句话说，你的模板文件的路径应该是polls/templates/polls/index.html.因为Django会寻找到对应的app_directiories，所以你只要使用polls/index.html就可以用到这一模板了。

            + **模板命名空间**
                + 虽然我们现在将模板 文件放在polls/templates文件中（而不是在建立一个polls文件夹），但是这样做不太好。Django将会选择第一个匹配的模板文件，如果你有一个模板文件正好和另一个应用中的某个模板文件重名，Django没有办法区分他们，我们需要帮助Django选择正确的模板，最简单的方法就是把他们放入各自的命名空间中，也就是吧这些模板放入一个和自身应用重名的子文件夹里。

        + 将下面的代码输入刚刚创建的模板文件中;

            + ```python
                {% if latest_question_list %}
                	<ul>
                    {% for question in latest_question_list %}
                    	<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a><li>
                    {% endfor %}
                    <ul>
                {% else %}
                	<p>No polls are available.</p>
                {% endif %}
                ```

        + 然后，让我们更新一下polls/views.py里的index视图来使用模板：

            + ```python
                from django.http import HttpResponse
                from django.template import loader
                
                from .models import Question
                
                def index(request):
                    latest_question_list = Question.objects.order_by('-						pub_date')[:5]
                    template = loader.get_template('polls/index.html')
                    context = {
                        'latest_question_list': latest_question_list,
                    }
                    return HttpResponse(template.render(context, request))
                ```

            + 上述代码的作用是，载入polls/index.html模板文件，并且向他传递一个上下文（context）。这个上下文字是一个***字典***，他将模板内的变量映射为Python对象。（在视图中载入模板，并且向它传递一个上下文）

    + #### 17、一个快捷函数：reander()

        + [**载入模板，填充上下文，在返回它生成的HttpResponse对象**]是一个非常常用的操作流程。于是Django提供了一个快捷函数，我们用它来重写index()视图：

            + ```python
                from django.shortcuts import reander
                
                from .model import Question
                
                def index(request):
                    latest_question_list = Question.objects.order_by('-pub_date')[:5]
                    context = {'latest_question_list': latest_question_list}
                    return render(request, 'polls/index.html', context)
                ```

            + 注意到，我们不在需要导入loader和HttpResponse。不过如果你还有其他函数（detail, results, 和vote）需要用到它的话，就主要保持HttpResponse的导入。

    + #### 18、抛出404错误

        + 现在，我们来处理投票详情视图 -- 他会指定投票的问题标题。下面是这个视图的代码：

        + ```python
            from django.http import Http404
            from django.shortcuts import render
            
            from .models import Question 
            
            def detail(request, question_id):
                try:
                    question = Question.objects.get(pk=question_id)
                except Question.DoesNotExist:
                    raise Http404("Question does not exist.")
            	return render(request, 'polls/detail.html', {'question': question})        
            ```

        + 这里有个新原则，如果指定问题ID对应的问题不存在，这个视图就会抛出一个Http404异常。  

    + #### 19、一个快捷函数：get_object_or_404()    

        + 尝试用get()函数获取一个对象，如果不存在就抛出Http404错误也是一个普遍的流程，Django也提供了一个快捷函数。下面是修改后的详情代码detail()视图的代码：       

        + ```python
            from django.shoortcuts import get_object_or_404, render
            from .model import Question
            
            def detail(request, question_id):
                question = get_object_or_404(Question, pk=question_id)
                return render(request, 'polls/detail.html', {'question': question})
            ```

        + get_object_or_404()函数将Django模型作为它的第一个参数和任意数量的关键字参数，并将这些参数传递给模型管理器的get()函数。如果对象不存在，它将引发Http404。

        + **设计哲学**

            + *为什么我们使用的辅助函数get_object_or_404()而不是自己捕获ObjectDoesNotExist异常呢？还有，为什么模型API不直接抛出ObjectDoesNotExist而是抛出Http404呢？*
            + *因为这样做会增加模型层和视图层的耦合性。知道Django设计的最重要的思想就是要保证松散耦合，一些受控制的耦合将会被包涵在django.shortcuts模块中。*

        + 也有get_list_or_404()函数，工作原理和get_object_or_404()一样，除了get()函数换成了filter()函数。如果列表为空的话，将会抛出Http404异常。

    + #### 20、使用模板系统

        + 回过头看看我们的detail()视图。它向模板传递上下文变量question。下面是polls/detail.html模板里正式的代码：

        + ```python
            <h1>{{ question.question_text }}</h1>
            <ul>
            {% for choice in question.choice_set.all %}
            	<li>{{ choice.choice_text }}</li>
            {% endfor %}
            </ul>
            
            ```

        + 模板系统统一使用点符号来访问变量的属性。在实例{{ question.question_text }}中，首先Django尝试随question对象使用字典查找（也就是使用obj,get(str)操作），如果失败了就尝试属性查找（也就是obj.str），结果成功了。如果这一操作也失败的话，将会尝试列表查找（也就是obj[int]）

        + 在{% for %}循环中发生的函数调用：question.choice_set.all被解释为Python代码question.choice_set.all()，将会返回一个可迭代的Choice对象，这一对象可以在{% for %}标签内部使用。

    + #### 21、去除模板中的硬编码URL

        + 还记得吗，我们在polls/index.html里编写投票连接时。连接时硬编码的：

        + ```python
            <li><a href='/polls/{{ question.id }}'>{{ question.question_text }}</a></li>
            ```

        + 问题在于，硬编码和强耦合的连接，碎玉一个包涵很多应用的项目来说，修改起来十分困难，然而，因为你在polls.urls的URl()函数中通过name参数URL定义了名字，你可以使用{% url %}

        + ```python
            <li><a href=“{% url 'detail' question.id %}”>{{ question.question_text }}</a></li>
            ```

        + 这个标签的工作方式是在polls.urls模块的URL定义中寻具有指定名字的条目，你可以回忆一下，具有名字‘detail’的URL是在如下语句中定义的：

        + ```python
            path('<int:question_id>/', views.detail, name='detail'),
            ```

        + 如果你想发别的视图的URL，比如想改成polls/specifics/12/，你不用在模板中修改任何东西（包括其他参数），只要在polls/urls.py里稍微修改一下就行：

        + ```python
            path('specifics/<int:question_id>/', views.detail, name='detail')
            ```

    + #### 22、为URL名称添加命名空间

        + 本项目只有一个应用，polls。在一个真实的Django项目中，可能会有五个，是个，二十个，甚至更多应用。Django如何分辨重名的URL呢？举个栗子。polls应用有detail视图，可能另一个博客应用也有同名的视图。Django如何知道{% url %}标签到底对应哪一哥应用的URL呢?

        + 答案是：在根URLconf中添加命名空间。在polls/urls.py文件中稍作修改。加上app_name设置命名空间：

        + ```python
            from django.urls import path
            
            from . import views
            
            app_name = 'polls'
            urlpatterns = [
                path('', views, index, name='index'),
                path('<int:question_id>/', views.results, name='results'),
                path('<int:question_id>/results', views.results, name = 'results'),
                path('<int:question_id>/vote/', views.vote, name='vote')
            ]
            ```

        + 现在，编辑polls/index.html文件，从：'detail'修改为‘polls:detail’

        + ```python
            <li><a href = "{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
            ```

+ ## 使用通用视图：代码还是少一点好

    + detail()和results9()视图都是很简单 -- 并且，向上面提到的那样，存在冗余问题，用来显示一个投票列表的index()视图和他们类似

        + 这些视图反映基本的Web开发中的一个常见的情况：根据URL中的参数从数据库中获取数据，载入模板文件然后返回渲染后的模板。由于这种情况特别常见，Django提供了一种快捷方式，叫做“通用视图”系统。
        + 通用视图将常见的模式抽象化，可以使你在编写应用时甚至不需要编写python代码。
        + 让我们将我们的投票应用转换成使用通用视图系统，这样我们可以删除许多我们的代码。我们仅仅需要做一下几步完成转换，我们将：
            + 转换URLconf。
            + 删除一些旧的、不在需要的视图。
            + 基于Django的通用视图引入新的视图。
        + 请继续阅读详细信息：
            + **为什么要重构代码？**
                + 一般来说，当编写一个Django应用时，你应该先评估一下通用视图是否可以解决你的问题，你应该在一开始使用它，而不是进行到一般时重构代码。本教程目前为止将重点放在以“艰难的方式”编写视图，这是为将重点放在核心概念上。
                + 就像在使用计算机之前你需要掌握基础数学一样。

    + #### 23、改良URLconf

        + 首先打开polls/urls.py这个URLconf并将它修改成：

        + ```python
            from django.urls import path
            
            from . import views
            
            app_name = 'polls'
            urlpatterns = [
                path('',views.IndexView.as_view(), name = 'index'),
                path('<int:pk>/', views.DetailView.as_view(), name='detail'),
                path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
                path('<int:question_id>/vote/', views.vote, name = 'vote'),
            ]
            ```

        + 注意，第二个和第三个匹配准则中，路径字符串中匹配模式的名称已经由<question_id>改为<pk>.

    + #### 24、改良视图

        + 下一步，我们将删除旧的index，detail,和results视图，并用Django通用视图代替。打开polls/views.py文件，并将它修改成：

        + ```python
            from django.http import HttpResponseRedirect
            from django.shortcuts import get_object_or_404, render
            from django.urls import reverse
            from django.views import generic
            
            from .models import Choice, Question
            
            class IndexView(genric.ListView):
                template_name = 'polls/index.html'
                context_object_name = 'latest_question_list'
                
                def get_queryset(self):
                    return Question.object.order_by('-pub_date')[:5]
                
            class DetailView(genric.DetailView):
                model = Question
                template = 'polls/detail.html'
              
            class ResultsView(genric.DetailView):
                model = Quesion
                template_name = 'polls/results.html'
                
                
                def vote(request, question_id):
                    ...# same as above, no changes needed.
            ```

        + 我们在这里使用两个通用视图：ListView和DetailView。这两个视图分别抽象“显示一个对象列表”和“显示一个特定类型对象的详细信息页面”这两种概念。

            + 每个视图需要知道他讲作用于那个模型，这由model属性提供。
            + DetailView期望从URL中捕获名为‘pk’的主键值，所以我们为通用视图把question_id改成pk。

+ ## 自动化测试简介

    + #### 25、自动化测试是什么？

        + 测试，是用来检查代码正确性的一些简单的程序。
        + 测试在不同的层次中都存在。有些测试值关注某个很小的细节（某个模型的某个方法返回值是否满足预期？），而另一些测试可能检查对某个软件的一系列操作（某一用户输入序列是否造成了预期的结果？）。其实这和我们在教程2部分，做的并没有什么不同，我们使用shell来测试某一方面的功能，或者运行某个应用并输入数据来检查它的行为。
        + 真正不同的地方在于，*自动化*测试是由某个系统帮你自动完成的，当你创建好了一系列测试。每次修改应用代码后，就可以自动检查出修改后的代码是否还像你曾经预期的那样正常工作。你不需要花费大量的时间来进行手动测试。

    + #### 26、为什么你需要写测试

        + **但是，为什么需要测试呢？有为什么是现在呢？**
            + 你可能觉得学python/Django对你来说已经很满足了，在学一些新的东西看起来有点负担过重并且没必要。毕竟，我们的投票应用看起来已经完美工作了。写一些自动测试并不能让它工作的更好，如果写一个投票是你想用Django完成的唯一工作，那你确实没必要学写测试。但是如果你还想写更复杂的项目，现在就是学习测试写法的做好时机了。
        + **测试将节约你的时间**
            + 在某种程度上，能够【判断出代码是否正常工作】的测试，就称得上是个令人满意的了。在复杂的应用程序中，组件之间可能会有数十个复杂的交互。
            + 在更加复杂的应用中您那个，各种组件之间的交互可能会及其的复杂。改变其中某一组件的行为，也也有可能造成意想不到的结果。判断【代码是否正常工作】意味着你需要大量的数据来完整的测试全代码的功能，以确保你的小小修改没有对应用整体造成破坏 -- 这台浪费时间了。
            + 尤其当你发现自动化测试能几秒中之内帮您完成这件事时，就更会觉得手动测试是在是太浪费时间了。当某人写出错误的代码时，自动化测试还能帮助你定位错误代码的位置。
            + 有时候你会觉得，和富有创造性和生产力的业务代码不起来，编写枯燥的测试代码实在是太无聊了，特别是当你知道你的代码完全没有问题的时候。
            + 然而，编写测试还是要花费几个小时的手测试的应用，或者为了某个小错误而虎乱翻看代码要有意义的多。
        + **测试不仅能发现错误，而且能预防错误**
            + 【测试是开发的对立面】，这种思想是不对的。
            + 如果没有测试，整个应用的行为意图会变得更加的不清晰。甚至当你在看在即的代码也是这样，有时候你需要仔细研读一段代码才能搞清楚它有什么用。
            + 而测试的出现改变了这种情况，测试就好像是从内部仔细检查你的代码，当有些地方出错时，这些地方将会变得很显眼 -- 就算你自己没有意识但那里写错了。
        + **测试使你的代码更具有吸引力**
            + 你也许遇到过这种情况：你编写了一个绝赞的软件，但是其他开发者卡都不看一眼，因为它缺少测试。没有测试的代码不值得信任。Django最初开发者之一的Jacob Kaplan-Moss说过：“项目规划时没有包含是不科学的。”
            + 其他开发者希望在正式使用你的代码前看到它通过了测试，这事你需要测试的另一个重要的原因。
        + **测试有利于团队的协作**
            + 前面的几点都是从单人开发的角度来说的，复杂的应用可能有团队维护。 测试的存在保证了协作者不会不小心破坏了了你的代码（也保证你不会不小心弄坏了他们的）。如果你想作为一个Django程序猿谋生的话，你必须擅长编写测试！

+ ## 测试的自出策略

    + **有好几种不同的方法写测试**

        + 一些开发者遵循“测试驱动”的开发原则，他们在写代码之前先写测试。这种方法看起来有点反直觉，但事实上，这和大多数人日常的做法是想吻合的。我们会先描述一个问题，然后写代码来解决他。【测试驱动】的开放方法只是将问题的藐视抽象为了Python的预试样例。
        + 更普遍的情况是，一个刚接触自动化测试的新手更倾向于先写代码，然后在写测试。虽然提前写测试可能更好，但是晚点写起码也不没有强。
        + 有时候很难决定从哪里开始下手测试。如果你才写了几千行Python代码，选择从哪里看是测试确实不怎么简单，如果是这种情况，那么在你下次修改代码（比如加新功能，或者修复Bug）之前写个测试是比较合理且有效的。
        + 所以，我们现在就开始吧。

    + #### 26、开始我们的第一个测试




