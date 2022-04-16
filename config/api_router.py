from django.urls import path, include
from rest_framework_nested import routers


from apps.announcements.api.viewsets import (
    AnnouncementViewSet,
    SubcategoryViewSet,
    CategoryViewSet
)

router = routers.SimpleRouter()
router.register(r"categories", CategoryViewSet)

category_router = routers.NestedSimpleRouter(router, r"categories", lookup="category")
category_router.register("subcategories", SubcategoryViewSet)

subcategory_router = routers.NestedSimpleRouter(category_router, r"subcategories", lookup="subcategory")
subcategory_router.register("announcements", AnnouncementViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(category_router.urls)),
    path(r'', include(subcategory_router.urls))
]
