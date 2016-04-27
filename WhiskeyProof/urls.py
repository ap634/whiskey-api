"""WhiskeyProof URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from whiskies.views import UserListCreate, UserDetail, WhiskeyList,\
    WhiskeyDetail, ReviewListCreate, ReviewDetailUpdateDelete,\
    TagSearchListCreate, TagSearchDetailUpdateDelete, TagListCreate,\
    TagDetailUpdateDelete

urlpatterns = [
    url(r'^users/$', UserListCreate.as_view(), name="list_users"),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name="detail_user"),

    url(r'^whiskey/$', WhiskeyList.as_view(), name="list_whiskey"),
    url(r'^whiskey/(?P<pk>\d+)/$', WhiskeyDetail.as_view(),
        name="detail_whiskey"),

    url(r'^review/$', ReviewListCreate.as_view(), name="list_review"),
    url(r'^review/(?P<pk>\d+)/$', ReviewDetailUpdateDelete.as_view(),
        name="detail_review"),

    url(r'^tag/$', TagListCreate.as_view(), name="list_tag"),
    url(r'^tag/(?P<pk>\d+)/$', TagDetailUpdateDelete.as_view(),
        name="detail_tag"),
    url(r'^tagsearch/$', TagSearchListCreate.as_view(), name="list_tagsearch"),
    url(r'^tagsearch/(?P<pk>\d+)/$', TagSearchDetailUpdateDelete.as_view(),
        name="detail_tagsearch"),

    url(r'^admin/', admin.site.urls),
]