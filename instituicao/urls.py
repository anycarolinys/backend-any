from . import views
from rest_framework.routers import DefaultRouter
from fisioterapeuta.views import FisioterapeutasPorInstituicaoViewSet

router = DefaultRouter()
router.register(r'', views.InstituicaoViewSet, basename='Instituicao')
router.register(r'(?P<instituicao_id>[^/.]+)/fisioterapeuta', FisioterapeutasPorInstituicaoViewSet, basename='listagem')
urlpatterns = router.urls
