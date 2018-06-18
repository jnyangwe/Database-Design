from django.urls import path, re_path
from . import views

app_name = 'dagr'

urlpatterns = [
    #path(r'', views.index, name='index'),
    re_path(r'^$', views.add_manually, name='add'),
    re_path(r'^message/(?P<message>\w+)/$', views.message, name='message'),
    re_path(r'^add/manually/$', views.add_manually, name='add_manually'),
    re_path(r'^add/url/$', views.add_url, name='add_url'),
    re_path(r'^add/file/$', views.add_file, name='add_file'),
    re_path(r'^add/category/$', views.add_category, name="add_category"),
    re_path(r'^add/keyword/$', views.add_keyword, name="add_keyword"),


    #re_path(r'^queries/$', views.queries, name='dagr_queries'),
    re_path(r'^metadata/$', views.metadata, name='metadata'),
    re_path(r'^reach/$', views.reach, name='reach'),
    re_path(r'^time/(?P<rang>\w+)/$', views.time_range, name='time-range'),
    re_path(r'^time/$', views.time, name='time'),
    re_path(r'^family/(?P<descendant>\w+)/$', views.descendant, name='descendant'),
    re_path(r'^update/(?P<guid>\d+)/$', views.update_dagr, name='update_dagr'),
    re_path(r'^delete/(?P<guid>\d+)/$', views.delete_dagr, name='delete_dagr'),

]
