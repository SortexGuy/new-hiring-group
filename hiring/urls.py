from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register(r'user', views.CreateUserView)
router.register(r'areas-conocimiento', views.AreasConocimientoViewSet)
router.register(r'bancos', views.BancosViewSet)
router.register(r'universidades', views.UniversidadesViewSet)
router.register(r'profesiones', views.ProfesionesViewSet)
router.register(r'usuarios', views.UsuariosViewSet)
router.register(r'empresas', views.EmpresasViewSet)
router.register(r'postulantes', views.PostulantesViewSet)
router.register(r'vacantes', views.VacantesViewSet)
router.register(r'postulaciones', views.PostulacionesViewSet)
router.register(r'contratos', views.ContratosViewSet)
router.register(r'experiencias-laborales', views.ExperienciasLaboralesViewSet)
router.register(r'nominas', views.NominasViewSet)
router.register(r'recibos', views.RecibosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('health/', views.health_check, name='health_check'),
]
