
from django.contrib import admin
from django.urls import path
from cms.views import homepage, insert
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage,name="homepage"),
    path("insert/",insert, name="insertpage")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 