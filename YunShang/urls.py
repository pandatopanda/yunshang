from django.urls import path
from. import views
from YunShang.views import username
urlpatterns=[
    path('',views.index,name='index'),
    path('username/',username,name='bieming'),
]