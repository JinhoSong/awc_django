from django.conf.urls import url
from django.urls import path
from django.views.generic.detail import DetailView
from .views import *
from django.contrib.auth import views as auth_view
app_name = 'awc'

urlpatterns = [
    path('', shared_main, name='shared_main'),
    path('page', shared_page, name='shared_page'),
    path('download', shared_download, name='shared_download'),
    path('test', shared_test, name='shared_test'),
    path('notice', shared_notice, name='shared_notice'),
    path('search_url', search_url, name='search_url'),
    path('search_file', search_file, name='search_file'),
    path('search_done', search_done, name='search_done'),
    path('show_space', show_space, name='show_space'),
    #path('file_upload/', file_upload, name='file_upload')
]
