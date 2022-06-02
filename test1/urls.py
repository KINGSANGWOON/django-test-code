"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# from user.views import index, redirect_test  

from user.views import get_user, index, redirect_test
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index_1"),
    path("redirect",redirect_test),
    path("get_user/<int:user_id>",get_user) # get_user의 user_id를 인자로 받기 위해서는 /<int:user_id> 자료형과 어떤 변수로 인자를 받아줄 것인지 작성해 줘야한다
    # int:user_id
    # int:user_id 같은 path안에 파라미터 값을 준다 해서 패스 파라미터라 부른다
    

]
