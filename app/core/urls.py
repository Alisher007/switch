from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()
admin.site.enable_nav_sidebar = False


urlpatterns = [
    path('', include('device.urls', namespace='device')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'switch admin'
admin.site.site_title = 'switch admin'
admin.site.site_url = 'http://localhost:8000/'
admin.site.index_title = 'switch administration'