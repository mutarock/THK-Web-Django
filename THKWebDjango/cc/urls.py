from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'events$', 'cc.views.events_new')
)
