from rest_framework.serializers import ModelSerializer

from apps.announcements.models import Announcement, Category, Subcategory


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"


class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"
