from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', views.AdministradorViewSet, basename='Administrador')
urlpatterns = router.urls
