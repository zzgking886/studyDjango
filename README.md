#studyDjango

django学习笔记

pip是一个很重要的python 安装工具，mac下一定要装他。

pip 安装python3，剩下的安装一些python库的时候要用 pip3 来确定是用python2.X来装还是3.X。

pip install django 来安装django。

pycharm 来进行django工程创建，在创建工程的时候有一个application要写上名字，这样才会有view，否则要自己创建。

rest_framework 是一个在url里面指定view的python库。可以很轻松的构建web api

添加数据库，现在model里面添加model的字段，也就是数据库的字段。

serializers 文件自己创建，写数据库解析

python manage.py makemigrations
python manage.py migrate

同步数据库命令

在view中写上post或者get方法，然后从数据库读取。

在mysql中 首先配置环境变量
打开终端,输入:
alias mysql=/usr/local/mysql/bin/mysql
alias mysqladmin=/usr/local/mysql/bin/mysqladmin

mysql -u root -p 命令进入数据库，可以操作 show tables ; 等操作。

配置服务器和gunicorn:

配置uswgi 失败，无法启动，改为 gunicorn     这个比较好用地址http://gunicorn.org/
配置完之后，运行命令 ： gunicorn -b 0.0.0.0:8000  --workers=2 zzgSystem.wsgi    
其中  zzgSystem代表django中app的名字。 workers 代表占用cpu的线程数。

http://tutos.readthedocs.io/en/latest/source/ndg.html

nginx 配置地址与端口http://127.0.0.1:8020

gunicorn 运行命令：gunicorn ×××.wsgi:application -b 127.0.0.1:8020 --reload(要到django的工程目录下。)

重启nginx 命令 先验证语法是否有错误：sudo nginx -t 。之后：sudo nginx -s reload

如果遇到nginx pid 启动错误 用这两句：
$ sudo nginx -c /usr/local/etc/nginx/nginx.conf
$ sudo nginx -s reload

对于css等样式文件缺失问题：
vim工具修改 nginx中配置 local /static/ 然后root 静态文件路径。
在django项目的url.py中添加如下代码:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
样式终于有了，搞了好几天啊！！！！！

正在配置nginx外网访问中...
