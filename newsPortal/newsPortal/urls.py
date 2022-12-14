
from django.contrib import admin
from django.urls import path
from cms.views import homepage, insert, viewPost, search
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage,name="homepage"),
    path("insert-post/",insert, name="insertpage"),
    path("category/<int:cat_id>/",viewPost, name="category"),
    path("search/",search, name="search"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 