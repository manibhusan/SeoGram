
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
admin.site.site_header = 'SeoGram'
admin.site.index_title = 'SeoGram'
admin.site.site_title = 'SeoGram Website'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
