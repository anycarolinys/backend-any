from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', views.ConsultaViewSet, basename='Consultas')
urlpatterns = router.urls
