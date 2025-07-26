from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        task = self.get_object()
        task.completed = not task.completed
        task.save()
        return Response(
            {'status': 'completed toggled', 'completed': task.completed}
        )

    @action(detail=False, methods=['get'])
    def stats(self, request):
        total = Task.objects.count()
        completed = Task.objects.filter(completed=True).count()
        pending = total - completed
        return Response(
            {'total': total, 'completed': completed, 'pending': pending}
        )


def health_check(request):
    return JsonResponse({'status': 'healthy', 'service': 'django-backend'})
