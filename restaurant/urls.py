from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, PlatoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'platos', PlatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 