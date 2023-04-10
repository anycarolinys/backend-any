from rest_framework.routers import DefaultRouter
from views import CircunstanciaViewSet

router = DefaultRouter()
router.register(r'', CircunstanciaViewSet, basename='Circunstancia')
urlpatterns = router.urls