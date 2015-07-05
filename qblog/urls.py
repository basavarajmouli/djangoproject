from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^', include('blog.urls')),
    #url(r'^images/(?P<path>.*)$', 'django.views.static.serve',
     #            {'document_root': settings.MEDIA_DIRS}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
