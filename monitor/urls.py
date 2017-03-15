# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('monitor.views',
    (r'^$', 'home'),
    (r'^(?P<test_id>[0-9]+)/$','index'),
    (r'^mul/$','mul'),
    (r'^jisuan$','jisuan'),
)
