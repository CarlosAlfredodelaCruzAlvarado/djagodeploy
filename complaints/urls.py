# complaints/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComplaintViewSet, get_complaints, CommentViewSet

router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas del router
    path('api/complaints/', get_complaints, name='get_complaints'),  # Ruta personalizada para obtener complaints
]
