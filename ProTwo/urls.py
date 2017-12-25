from django.conf.urls import url
from . import views
#template tagging
app_name = 'protwo'
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$',views.user_login, name='user_login'),
    url(r'^relative/$', views.relative, name ='relative'),
    url(r'^other/$',views.other, name='other'),
    url(r'^base/$',views.base, name='base'),
]
