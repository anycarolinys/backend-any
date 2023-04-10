from rest_framework.routers import DefaultRouter
from .views import FormAFMViewSet

router = DefaultRouter()
router.register(r'', FormAFMViewSet, basename='FormAFM')
urlpatterns = router.urls