from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .models import (
    AreasConocimiento,
    Bancos,
    Universidades,
    Profesiones,
    Usuarios,
    Empresas,
    Postulantes,
    Vacantes,
    Postulaciones,
    Contratos,
    ExperienciasLaborales,
    Nominas,
    Recibos,
)
from .serializers import (
    AreasConocimientoSerializer,
    BancosSerializer,
    UniversidadesSerializer,
    ProfesionesSerializer,
    UsuariosSerializer,
    EmpresasSerializer,
    PostulantesSerializer,
    VacantesSerializer,
    PostulacionesSerializer,
    ContratosSerializer,
    ExperienciasLaboralesSerializer,
    NominasSerializer,
    RecibosSerializer,
    UserSerializer,
)


# from .models import Task

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#     @action(detail=True, methods=['post'])
#     def toggle_complete(self, request, pk=None):
#         task = self.get_object()
#         task.completed = not task.completed
#         task.save()
#         return Response(
#             {'status': 'completed toggled', 'completed': task.completed}
#         )
#
#     @action(detail=False, methods=['get'])
#     def stats(self, request):
#         total = Task.objects.count()
#         completed = Task.objects.filter(completed=True).count()
#         pending = total - completed
#         return Response(
#             {'total': total, 'completed': completed, 'pending': pending}
#         )


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class AreasConocimientoViewSet(viewsets.ModelViewSet):
    queryset = AreasConocimiento.objects.all()
    serializer_class = AreasConocimientoSerializer


class BancosViewSet(viewsets.ModelViewSet):
    queryset = Bancos.objects.all()
    serializer_class = BancosSerializer


class UniversidadesViewSet(viewsets.ModelViewSet):
    queryset = Universidades.objects.all()
    serializer_class = UniversidadesSerializer


class ProfesionesViewSet(viewsets.ModelViewSet):
    queryset = Profesiones.objects.all()
    serializer_class = ProfesionesSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

    # def list(self, request):
    #     pass
    #
    # def retrieve(self, request, pk=None):
    #     pass


class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer


class PostulantesViewSet(viewsets.ModelViewSet):
    queryset = Postulantes.objects.all()
    serializer_class = PostulantesSerializer


class VacantesViewSet(viewsets.ModelViewSet):
    queryset = Vacantes.objects.all()
    serializer_class = VacantesSerializer


class PostulacionesViewSet(viewsets.ModelViewSet):
    queryset = Postulaciones.objects.all()
    serializer_class = PostulacionesSerializer


class ContratosViewSet(viewsets.ModelViewSet):
    queryset = Contratos.objects.all()
    serializer_class = ContratosSerializer


class ExperienciasLaboralesViewSet(viewsets.ModelViewSet):
    queryset = ExperienciasLaborales.objects.all()
    serializer_class = ExperienciasLaboralesSerializer


class NominasViewSet(viewsets.ModelViewSet):
    queryset = Nominas.objects.all()
    serializer_class = NominasSerializer


class RecibosViewSet(viewsets.ModelViewSet):
    queryset = Recibos.objects.all()
    serializer_class = RecibosSerializer


def health_check(request):
    return JsonResponse({'status': 'healthy', 'service': 'django-backend'})
