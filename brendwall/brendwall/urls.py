from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")

urlpatterns = [
    path('ajax/', include('ajax.urls')),
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
]
