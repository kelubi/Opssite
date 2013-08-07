from django.conf.urls import patterns, include, url
#from opssite.views import hello,current_datetime,hours_ahead,archive
from opssite import views, update
#from contact import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', views.hello),
    (r'^update/(.*)/$', update.get_apps),
    (r'^update/(.*)/(.*)$', update.get_servers),
#    (r'^archive/$', views.archive),
#    (r'^search-form/$', views.search_form),
#    (r'^search/$', views.search),
#    (r'^contact/$', views.contact),
#    ('^time/$', views.current_datetime),
#    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    # Examples:
    # url(r'^$', 'opssite.views.home', name='home'),
    # url(r'^opssite/', include('opssite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'', include(admin.site.urls)),
    #url(r'^admin/', include(admin.site.urls)),
)
