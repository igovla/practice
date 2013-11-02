from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pages.views.home'),
    url(r'^log/(?P<diry>([-,.\w]*/)*)$','pages.views.listing'),
    url(r'^library/$', 'pages.views.books'),
    url(r'^library/books/$', 'pages.views.books'),
    url(r'^library/books/(\d+)/$', 'pages.views.book'),
    url(r'^library/authors/$', 'pages.views.authors'),
    url(r'^library/authors/(\d+)/$', 'pages.views.author'),
    # Examples:
    # url(r'^$', 'control_panel.views.home', name='home'),
    # url(r'^control_panel/', include('control_panel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
