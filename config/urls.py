from django.contrib import admin
from django.urls import path, include

from .swagger import urlpatterns as swagger_urlpatterns
from .api_router import urlpatterns as api_urlpatterns

from apps.announcements.api.views import LatestAnnouncements


urlpatterns = [
    path("admin/", admin.site.urls),
    path("latest-announcements/", LatestAnnouncements.as_view())
]

urlpatterns += swagger_urlpatterns
urlpatterns += api_urlpatterns
