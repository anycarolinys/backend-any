from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', views.PacienteViewSet, basename='Paciente')
urlpatterns = router.urls
