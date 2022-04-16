from rest_framework.generics import ListAPIView

from .serializers import AnnouncementSerializer, Announcement


class LatestAnnouncements(ListAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.order_by("-date")
