from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from .serializers import CategorySerializer, SubcategorySerializer, AnnouncementSerializer
from apps.announcements.models import Category, Subcategory, Announcement


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=["GET"], detail=True)
    def announcements(self, request, pk=None):
        announcements = Announcement.objects.filter(subcategory__category_id=pk)
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
