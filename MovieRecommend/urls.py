"""MovieRecommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from index import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('hello/',views.hello),
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('index/', include("index.urls")),
    path('login/',include("login.urls")),
    path('register/',include('register.urls')),
]
'''
path(route, view, kwargs=None, name=None)

route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。

view: 用于执行与正则表达式匹配的 URL 请求。

kwargs: 视图使用的字典类型的参数。

name: 用来反向获取 URL。
'''