from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Tasks

# Create your views here.
class TasksView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Tasks.objects.all()