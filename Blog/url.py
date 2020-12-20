from django.urls import path,re_path
from . import api_views,views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework import status

status


app_name = 'Blog'
urlpatterns = [
path('', views.index), 

# api 
path('api', api_views.create_api), 
path('api/token', TokenObtainPairView.as_view()),
path('api/<int:pk>', api_views.detail_api), 
re_path(r'api-blog/(?P<slug>[0-9 a-z A-Z -]*)/$', api_views.api_blog), 
path('api-blog', api_views.api_allblog)
]