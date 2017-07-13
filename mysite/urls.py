from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Sign twitter's urls by the url file.
    url(r'^twitter/', include('twitter.urls')),
    url(r'^admin/', admin.site.urls),
]
