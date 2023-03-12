from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from datacenter import views

urlpatterns = [
    url(r'^$', views.view_classes, name='classes'),
    url(r'^(?P<year>[\w+ ]+)/(?P<letter>[\w+ ]+)$', views.view_class_info,
        name='class_info'),
    url(r'^(?P<year>[\w+ ]+)/(?P<letter>[\w+ ]+)/schedule/$',
        views.view_schedule, name='schedule'),
    url(r'^(?P<year>[\w+ ]+)/(?P<letter>[\w+ ]+)/schedule/$',
        views.view_schedule, name='schedule'),
    url(r'^schoolkid/(?P<schoolkid_id>[\w+ ]+)/$', views.view_schoolkid,
        name='schoolkid'),
    url(
        r'^journal/'
        r'(?P<year>[\w+ ]+)/'
        r'(?P<letter>[\w+ ]+)/'
        r'(?P<subject_id>[\w+ ]+)/$',
        views.view_journal, name='journal'),
]

urlpatterns += staticfiles_urlpatterns()
