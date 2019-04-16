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

        + *现在开发这个“项目”环境已经配置好了，就可以开始干活了*

        + *在Django中每一个应用都是一个Python包，并且遵循着形同的约定。Django自带一个工具，可以帮您生成应用的基础结构，这样你就能专心的写代码了，而不是创建目录*

            + ##### 项目VS应用

            + 项目和应用有什么区别？

                + 1、应用是专门做某件是的网络应用程序--比如博客系统，或者公共记录的数据库，或者简单的投票程序。
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

        + 在mysite/urls.py 文件的urlpatterns列表中cherub一个include() , 如下：

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

        + 现在，打开nysite/settings.py,这是个包含Django项目设置的Python模块

        + 通常这个配置文件中使用SQLite作为默认数据库

        + 如果想使用其他的数据库，就需要安装合适的引擎，然后在设置文件中*DATABASE"default"*项目中的一些键值：

            + **ENGINE-- 可选值有**：

                + "django.db.backends.sqlite3","django.db.backends.postgresql",
                + "django.db.backends.oracle","django.db.backends.mysql"

            + **NAME** --数据库名称 

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

                + **django.contrib.admin** -- 管理员站点，
                + **django.contrib.auth** -- 认证授权系统
                + **django.contrib.contenttypes** -- 内容类型框架
                + **django.contrib.sessions** -- 会话框架
                + **django.contrib.messages** -- 消息框架
                + **django**.**contrib.staticfiles** -- 管理静态文件的框架

            + ***这些应用被默认启用是为了给常规项目提供方便***

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

            + 因为**PollsConfig**类写在文件**polls/apps.py**中，所以它是我点式路径是“**polls.apps.PollsConfig**”

                + 在文件mysite/settings.py中INSTALLED_APPS子项添加点式路径

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

            + 这个命令是migrate，我们马上回接触它

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

        +  如果你敢兴趣，你也可以试试运行python manage.py check ,这个命令帮助检查项目中的问题，并且在检查过程中不会对数据库进行任何操作。

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

        + 迁移的功能非常强大，它能让你在开发过程中持续的改变数据库结构儿不需要重新删除和创建表 - 它专注于使数据据平滑升级而不会丢失数据。

        + 现在，我们只需要记住，改变模型需要三步：

            + 编辑models.py 文件，改变模型。
            + 运行python  manage.py makemigrations 为模型的改变生成迁移文件
            + 运行python manage.py migrate 来应用数据库迁移

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

    + #### 一个真正有用的视图

        + 每个视图必须    含被请求页面内容的HttpResponse对象，或者抛出一个异常，比如Http404.

        + 你的视图可以从数据库里读取数据记录，可以使用一个引擎模板（比如Django自带的，或者其他第三方的），可以生成一个PDF文件，可以输出一个XML，创建一个ZIP文件，你可以做任何您想做的事，使用任何你想用的pythopn库。

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
                + 虽然我们现在将模板 文件放在polls/templates文件中（而不是在建立一个polls文件夹），但是这样做不太好。Django将会选择第一个匹配的模板文件，如果你有一个模板文件正好和另一个应用中的某个模板文件重名，Django没有办法区分他们，我们需要帮助Django选择正确的模板，最简单的方法就是把他们放入各自的命名空间中，也就是吧这些模板放入一个和自身应用重名的字文件夹里。

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

            + 上述代码的作用是，载入polls/index.html模板文件，并且向他传递一个上下文（context）。这个上下文字是一个字典，他讲模板内的变量映射为Python对象。

