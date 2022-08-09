from django.urls import re_path as url
from django.urls import include
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('blog.urls')),
]