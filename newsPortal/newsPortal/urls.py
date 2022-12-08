
from django.contrib import admin
from django.urls import path
from cms.views import homepage, insert

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage,name="homepage"),
    path("insert/",insert, name="insertpage")
]
